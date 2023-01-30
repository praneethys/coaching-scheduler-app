<template>
  <div class="container">
    <h4 class="mt-4">My Dashboard</h4>
    <div class="mt-4 card">
      <h6 class="left">Please select begin time of your availability.</h6>
      <div class="form-row">
        <div class="col">
          <label
            >Session Begin Time<input
              class="mx-2 align-left"
              type="datetime-local"
              v-model="beginDate"
              min="new Date()"
          /></label>
        </div>
      </div>
      <h6 class="mt-2">
        Selected session time slot: {{ formatDateTime(beginDate) }} -
        {{ formatDateTime(endDate) }} ({{ getTimezone(beginDate) }})
      </h6>
      <button
        class="mt-2 btn btn-primary"
        @click="setAvailability"
        type="button"
      >
        Set Availability
      </button>
    </div>
    <div class="mt-4 card">
      <h5 class="mt-2">My Schedules</h5>
      <table class="table table-hover mt-2">
        <thead>
          <th>Select for feedback</th>
          <th>Time Slot</th>
          <th>Student ID</th>
        </thead>
        <tbody>
          <tr v-for="sch in schedules" :key="sch.id">
            <td>
              <input
                type="radio"
                v-model="selectedSchedule"
                :value="sch"
                @change="getFeedbackByScheduleId"
              />
            </td>
            <td>
              {{ formatDateTime(sch.begin_time) }} -
              {{ formatDateTime(sch.end_time) }}
              {{ getTimezone(sch.begin_time) }}
            </td>
            <td>
              {{ sch.student_id !== -1 ? sch.student_id : "" }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="mt-4 card">
      <div v-if="feedbackForSchedule.length > 0">
        <h6>Feedback History</h6>
        <table class="table table-hover mt-2">
          <thead>
            <th>Schedule ID</th>
            <th>Satisfaction Rating</th>
            <th>Notes</th>
          </thead>
          <tbody>
            <tr v-for="sch in feedbackForSchedule" :key="sch.schedule_id">
              <td>{{ sch.schedule_id }}</td>
              <td>{{ sch.rating }}</td>
              <td>{{ sch.notes }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div v-else-if="selectedSchedule.student_id !== -1">
        <h6>Prodvide Feedback</h6>
        <div class="form-row mt-4">
          <div class="col">
            <label
              >Satisfaction Rating (1-5)<input
                type="number"
                class="mx-2 align-left"
                v-model="satisfactionRating"
                min="1"
                max="5"
            /></label>
          </div>
        </div>
        <div class="form-row">
          <div class="col">
            <textarea
              type="textbox"
              v-model="feedbackNotes"
              class="mx-2 align-right"
              spellcheck="true"
              rows="3"
              placeholder="Write your notes here"
            />
          </div>
        </div>
        <button
          type="button"
          class="mt-4 btn btn-primary"
          @click="submitFeedback"
        >
          Submit Feedback
        </button>
      </div>
    </div>
    <div>
      <button
        type="button"
        class="mt-4 btn"
        @click="$router.push({ name: 'home' })"
      >
        Go Back
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import { httpClient } from "@/util/httpUtil";
import { defineComponent } from "vue";
import moment from "moment";
import { ISchedule, IFeedbackResponse } from "@/util/interface";
import { formatDateTime, getTimezone } from "@/util/format";

export default defineComponent({
  name: "CoachView",
  data: function () {
    return {
      formatDateTime,
      getTimezone,
      beginDate: new Date(),
      schedules: [] as ISchedule[],
      selectedSchedule: {
        id: -1,
        coach_id: -1,
        student_id: -1,
        begin_time: null,
        end_time: null,
      },
      feedbackForSchedule: [] as IFeedbackResponse[],
      moment,
      satisfactionRating: null,
      feedbackNotes: "",
    };
  },
  props: {
    coachId: String,
  },
  mounted: async function () {
    console.log(`${this.$route.path} mounted`);
    await this.getSchedule();
  },
  methods: {
    getSchedule: async function () {
      try {
        const response = await httpClient.post("/getScheduleByCoach", {
          coach_id: this.coachId,
        });
        this.schedules = response.data;
        console.log(`getSchedule: ${JSON.stringify(this.schedules)}`);
      } catch (e) {
        console.error(e);
      }
    },
    setAvailability: async function () {
      try {
        console.log(`setAvailability`);
        const response = await httpClient.post("/setCoachAvailability", {
          coach_id: this.coachId,
          begin_time: moment(this.beginDate).utc(),
          end_time: moment(this.endDate).utc(),
        });
        console.log(`setAvailability: ${JSON.stringify(response.data)}`);
        await this.getSchedule();
      } catch (e) {
        console.error(e);
      }
    },
    getFeedbackByScheduleId: async function () {
      try {
        console.log("getFeedbackByScheduleId");
        const response = await httpClient.post("/getFeedbackByScheduleId", {
          schedule_id: this.selectedSchedule.id,
        });
        console.log(
          `getFeedbackByScheduleId: ${JSON.stringify(response.data)}`
        );
        this.feedbackForSchedule = response.data;
      } catch (e) {
        console.error(e);
      }
    },
    submitFeedback: async function () {
      try {
        console.log(`submitFeedback`);
        const response = await httpClient.post("/submitFeedbackByScheduleId", {
          schedule_id: this.selectedSchedule.id,
          rating: this.satisfactionRating,
          notes: this.feedbackNotes,
        });
        console.log(
          `submitFeedbackByScheduleId: ${JSON.stringify(response.data)}`
        );
        await this.getFeedbackByScheduleId();
      } catch (e) {
        console.error(e);
      } finally {
        this.satisfactionRating = null;
        this.feedbackNotes = "";
      }
    },
  },
  computed: {
    endDate: function () {
      return moment(this.beginDate).add(2, "hours").toDate();
    },
  },
});
</script>
