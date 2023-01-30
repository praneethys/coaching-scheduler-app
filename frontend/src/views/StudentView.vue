<template>
  <div class="container">
    <h5 class="mt-4">My Dashboard</h5>
    <div class="mt-4 card">
      <h5 class="mt-2">Upcoming</h5>
      <table class="table table-hover mt-2">
        <thead>
          <th>Time Slot</th>
          <th>Coach ID</th>
        </thead>
        <tbody>
          <tr v-for="sch in mySchedules" :key="sch.id">
            <td>
              {{ formatDateTime(sch.begin_time) }} -
              {{ formatDateTime(sch.end_time) }}
              {{ getTimezone(sch.begin_time) }}
            </td>
            <td>
              {{ sch.coach_id }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="mt-5 card">
      <h5 class="mt-2">Available Schedules</h5>
      <table class="table table-hover mt-4">
        <thead>
          <th>Selection</th>
          <th>Time Slot</th>
          <th>Coach ID</th>
        </thead>
        <tbody>
          <tr v-for="sch in availableSchedules" :key="sch.id">
            <td>
              <input type="radio" v-model="selectedSchedule" :value="sch" />
            </td>
            <td>
              {{ formatDateTime(sch.begin_time) }} -
              {{ formatDateTime(sch.end_time) }}
              {{ getTimezone(sch.begin_time) }}
            </td>
            <td>
              {{ sch.coach_id }}
            </td>
          </tr>
        </tbody>
      </table>
      <button
        type="button"
        class="mt-4 btn btn-primary"
        @click="setAppointment"
      >
        Schedule Appointment
      </button>
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
import { defineComponent } from "vue";
import { ISchedule } from "@/util/interface";
import { httpClient } from "@/util/httpUtil";
import moment from "moment";
import { formatDateTime, getTimezone } from "@/util/format";

export default defineComponent({
  name: "StudentView",
  data: function () {
    return {
      availableSchedules: [] as ISchedule[],
      mySchedules: [] as ISchedule[],
      selectedSchedule: {
        id: -1,
        coach_id: -1,
        student_id: -1,
        begin_time: null,
        end_time: null,
      },
      moment,
      formatDateTime,
      getTimezone,
    };
  },
  props: {
    studentId: String,
  },
  mounted: async function () {
    console.log(`${this.$route.path} mounted`);
    await this.getSchedule();
    await this.getAllAvailableAppointments();
  },
  methods: {
    getSchedule: async function () {
      try {
        const response = await httpClient.post("/getScheduleByStudent", {
          student_id: this.studentId,
        });
        this.mySchedules = response.data;
        console.log(`getSchedule: ${JSON.stringify(this.mySchedules)}`);
      } catch (e) {
        console.error(e);
      }
    },
    setAppointment: async function () {
      try {
        const response = await httpClient.post("/setAppointment", {
          student_id: this.studentId,
          schedule_id: this.selectedSchedule.id,
        });
        console.log(`setAppointment: ${JSON.stringify(response.data)}`);
        await this.getSchedule();
        await this.getAllAvailableAppointments();
      } catch (e) {
        console.error(e);
      }
    },
    getAllAvailableAppointments: async function () {
      try {
        const response = await httpClient.get("/getAllAvailableAppointments");
        this.availableSchedules = response.data;
        console.log(`getSchedule: ${JSON.stringify(this.availableSchedules)}`);
      } catch (e) {
        console.error(e);
      }
    },
  },
});
</script>
