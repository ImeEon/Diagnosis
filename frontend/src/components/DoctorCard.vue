<template>
  <el-card shadow="hover" class="doctor-card">
    <div style="display: flex">
      <div class="left">
        <el-image
          class="avatar"
          :src="avatar"
          :preview-src-list="[avatar]"
        ></el-image>
      </div>
      <div class="right">
        <el-descriptions :title="username" column="1" border="true">
          <el-descriptions-item label="真实姓名">
            {{ name }}
          </el-descriptions-item>
          <el-descriptions-item label="手机号">{{ tel }}</el-descriptions-item>
          <el-descriptions-item label="个人简介">
            {{ intro }}
          </el-descriptions-item>
        </el-descriptions>
        <div>
          <el-button type="success" class="button" @click="dateClicked">
            预约
          </el-button>
          <el-button type="primary" class="button" @click="logClicked">
            留言
          </el-button>
        </div>
      </div>
    </div>
  </el-card>
</template>

<script>
import axios from 'axios';
import { ElMessage } from 'element-plus';
export default {
  name: 'DoctorCard',
  props: ['username'],
  data: function () {
    return {
      birth: '',
      tel: '',
      intro: '',
      name: '',
      avatar: '',
    };
  },
  methods: {
    dateClicked() {
      ElMessage.warning('TODO');
    },
    logClicked() {
      ElMessage.warning('TODO');
    },
    getAvatar() {
      const that = this;
      axios
        .post(that.$store.getters.URL_GET_AVATAR, {
          username: that.username,
        })
        .then(function (response) {
          if (response.data.flag === true) {
            console.log(response);
            that.avatar =
              that.$store.getters.AVATER_IMAGE_BASE + response.data.avatar;
          } else {
            ElMessage.warning('获取头像失败');
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    getInfo() {
      const that = this;
      axios
        .post(that.$store.getters.URL_GET_DOCTOR_INFO, {
          username: that.username,
        })
        .then(function (response) {
          if (response.data.flag === true) {
            console.log(response);
            that.name = response.data.name;
            that.birth = response.data.birth;
            that.tel = response.data.tel;
            that.intro = response.data.intro;
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
    const that = this;
    that.getAvatar();
    that.getInfo();
  },
};
</script>

<style scoped>
.doctor-card {
  margin-bottom: 10px;
}
.left {
  display: flex;
  width: 200px;
  height: auto;
  text-align: center;
  flex-direction: column;
  margin-right: 10px;
}
.right {
  display: flex;
  flex-direction: column;
}
.button {
  width: 80px;
  margin-top: 10px;
}
</style>
