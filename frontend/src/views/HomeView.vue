<template>
  <div class="home mt-4">
    <div v-if="mode === MODE.NONE">
      <input v-model="userName" placeholder="User Name" />
      <div class="mt-3">
        <button
          type="button"
          class="col-sm-2 align-left btn btn-primary mx-2"
          @click="loginAsCoach"
        >
          I'm a Coach
        </button>
        <button
          type="button"
          class="col-sm-2 align-right btn btn-primary mx-2"
          @click="loginAsStudent"
        >
          I'm a Student
        </button>
      </div>
    </div>
    <div v-else-if="mode === MODE.COACH">Welcome Coach, {{ name }}!</div>
    <div v-else-if="mode === MODE.STUDENT">Welcome Student, {{ name }}!</div>
    <button
      v-if="mode !== MODE.NONE"
      type="button"
      class="btn btn-primary mt-4"
      @click="mode = MODE.NONE"
    >
      Go Home
    </button>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { httpClient } from "@/util/httpUtil";
// import HelloWorld from "@/components/HelloWorld.vue"; // @ is an alias to /src

enum MODE {
  NONE,
  COACH,
  STUDENT,
}

export default defineComponent({
  name: "HomeView",
  components: {
    // HelloWorld,
  },
  data: function () {
    return {
      userName: "",
      name: "",
      MODE,
      mode: MODE.NONE,
    };
  },
  mounted() {
    this.mode = MODE.NONE;
  },
  methods: {
    loginAsCoach: async function () {
      this.mode = MODE.COACH;
      try {
        const response = await httpClient.post("/getCoachByUserName", {
          user_name: this.userName,
        });

        const responsePayload = response.data[0];
        this.name = responsePayload.name;
        console.log(response.data);
        await this.$router.push({
          name: "coach",
          params: { coachId: responsePayload.id },
        });
      } catch (e) {
        console.error(e);
        this.mode = MODE.NONE;
      }
    },
    loginAsStudent: async function () {
      this.mode = MODE.STUDENT;
      try {
        const response = await httpClient.post("/getStudentByUserName", {
          user_name: this.userName,
        });

        const responsePayload = response.data[0];
        this.name = responsePayload.name;
        console.log(response.data);
        await this.$router.push({
          name: "student",
          params: { studentId: responsePayload.id },
        });
      } catch (e) {
        console.error(e);
        this.mode = MODE.NONE;
      }
    },
  },
});
</script>
