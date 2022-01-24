<template>
  <el-card shadow="hover" class="card">
    <div>
      <el-upload
        :action="$store.getters.URL_SET_AVATAR"
        :headers="{ username: $store.getters.username }"
        multiple="false"
        :name="$store.getters.username"
        :on-success="uploadSuccess"
        :show-file-list="false"
      >
        <el-avatar fit="cover" :size="120" :src="avatar"></el-avatar>
      </el-upload>
    </div>

    <div style="padding: 14px">
      <div>{{ $store.getters.username }}</div>
      <div>{{ $store.getters.usertype }}</div>
    </div>
  </el-card>
</template>

<script>
import axios from 'axios';
import { ElMessage } from 'element-plus';
export default {
  name: 'AvatarCard',
  data: function () {
    return {
      avatar: '',
    };
  },
  mounted: function () {
    this.getAvatar();
  },
  methods: {
    getAvatar() {
      const that = this;
      axios
        .post(that.$store.getters.URL_GET_AVATAR, {
          username: that.$store.getters.username,
        })
        .then(function (response) {
          if (response.data.flag === true) {
            that.avatar =
              that.$store.getters.AVATER_IMAGE_BASE + response.data.avatar;
          } else {
            ElMessage.error('获取头像失败');
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    uploadSuccess(response) {
      console.log(response);
      if (response.flag) {
        ElMessage.success('上传头像成功');
        this.getAvatar();
      } else {
        ElMessage.error('上传头像失败');
      }
    },
  },
};
</script>

<style scoped>
.card {
  margin-bottom: 10px;
  width: 100%;
  height: auto;
  text-align: center;
}
</style>
