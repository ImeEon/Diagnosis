<template>
  <el-card shadow="hover" id="patient-info-card">
    <el-form ref="form" :model="form" label-width="80px">
      <h2>{{ $store.getters.usertype }}</h2>
      <el-form-item label="真实姓名">
        <el-input
          v-model="form.name"
          type="text"
          :disabled="!editing"
        ></el-input>
      </el-form-item>
      <el-form-item label="出生日期">
        <el-date-picker
          type="date"
          placeholder="选择日期"
          v-model="form.birth"
          style="width: 100%"
          :disabled="!editing"
        ></el-date-picker>
      </el-form-item>
      <el-form-item label="电话">
        <el-input v-model="form.tel" type="tel" :disabled="!editing"></el-input>
      </el-form-item>
      <el-form-item label="个人介绍">
        <el-input
          type="textarea"
          v-model="form.intro"
          :autosize="{ minRows: 4, maxRows: 10 }"
          :disabled="!editing"
        ></el-input>
      </el-form-item>
      <el-form-item>
        <el-button v-if="!editing" type="primary" @click="onEdit">
          编辑
        </el-button>
        <el-button v-if="editing" type="success" @click="onSubmit">
          提交
        </el-button>
      </el-form-item>
    </el-form>
  </el-card>
  <router-view />
</template>

<script>
import axios from 'axios';
import { ElMessage } from 'element-plus';
export default {
  name: 'PatientInfo',
  components: {},
  data() {
    return {
      editing: false,
      form: {
        name: '',
        birth: '',
        tel: '',
        intro: '',
      },
    };
  },
  methods: {
    onEdit() {
      this.editing = true;
    },
    onSubmit() {
      this.editing = false;
      const that = this;
      axios
        .post(that.$store.getters.URL_SET_PATIENT_INFO, {
          username: that.$store.getters.username,
          name: that.form.name,
          birth: String(that.form.birth),
          tel: that.form.tel,
          intro: that.form.intro,
        })
        .then(function (response) {
          console.log(response);
          if (response.data.flag === true) {
            ElMessage.success('修改个人信息成功!');
          } else {
            ElMessage.error('修改个人信息失败!');
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
  mounted: function () {
    const that = this;
    axios
      .post(that.$store.getters.URL_GET_PATIENT_INFO, {
        username: that.$store.getters.username,
      })
      .then(function (response) {
        console.log(response);
        const data = response.data;
        if (data.flag === true) {
          that.form.name = data.name;
          that.form.birth = data.birth;
          that.form.tel = data.tel;
          that.form.intro = data.intro;
        } else {
          ElMessage.warning('暂无个人信息!');
        }
      })
      .catch(function (error) {
        console.log(error);
      });
  },
};
</script>

<style scoped>
#patient-info-card {
  width: auto;
  height: auto;
  padding: 20px;
}
</style>
