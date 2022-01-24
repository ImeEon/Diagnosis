<template>
  <div id="bg">
    <div id="main">
      <div id="left">
        <avatar-card></avatar-card>
        <navigation></navigation>
      </div>
      <div id="right">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
import Navigation from '../components/Navigation.vue';
import AvatarCard from '../components/AvatarCard.vue';
import { mapGetters } from 'vuex';
import { ElMessage } from 'element-plus';
import axios from 'axios';
export default {
  name: 'Main',
  components: {
    Navigation,
    AvatarCard,
  },
  computed: {
    ...mapGetters(['username']),
  },
  data: function () {
    return {};
  },
  methods: {
    getUserType() {
      const that = this;
      axios
        .post(that.$store.getters.URL_GET_USERTYPE, {
          username: that.$store.getters.username,
        })
        .then(function (response) {
          if (response.data.flag === true) {
            console.log(response);
            that.$store.commit('setUsertype', response.data.usertype);
          } else {
            ElMessage.error('获取用户类型失败');
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
  mounted() {
    this.getUserType();
  },
};
</script>

<style scoped>
#bg {
  background-color: rgb(237, 241, 241);
  width: 100%;
  height: 100%;
}
#main {
  width: 80%;
  height: 100%;
  margin-left: 10%;
  overflow: hidden;
  display: flex;
}
#left {
  width: 300px;
  height: 100%;
  display: flex;
  flex-direction: column;
  margin-right: 20px;
  padding-top: 10px;
}
#right {
  min-width: 800px;
  width: auto;
  height: 100%;
  padding-top: 10px;
  padding-bottom: 10px;
}
</style>
