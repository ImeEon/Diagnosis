<template>
  <el-scrollbar height="100%">
    <div class="doctors-card">
      <doctor-card
        v-for="(doctor, index) in doctors"
        v-bind:key="index"
        :username="doctor"
      ></doctor-card>
    </div>
  </el-scrollbar>
</template>

<script>
import axios from 'axios';
import { ElMessage } from 'element-plus';
import DoctorCard from './DoctorCard.vue';
export default {
  name: 'Doctors',
  components: {
    DoctorCard,
  },
  data: function () {
    return {
      doctors: [],
    };
  },
  methods: {
    getDoctors() {
      const that = this;
      axios
        .get(that.$store.getters.URL_GET_ALL_DOCTOR_USERNAME)
        .then(function (response) {
          if (response.data.flag === true) {
            console.log(response);
            that.doctors = response.data.doctors;
          } else {
            ElMessage.warning('暂无医生数据');
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
  mounted: function () {
    this.getDoctors();
  },
};
</script>

<style scoped>
.doctors-card {
  width: auto;
  height: 100%;
  padding-left: 20px;
  padding-right: 20px;
}
</style>
