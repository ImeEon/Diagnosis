<template>
  <div id="login">
    <el-card id="login-card">
      <el-tabs v-model="active" @tab-click="handleClick" stretch>
        <el-tab-pane label="注册" name="signup">
          <sign-up></sign-up>
        </el-tab-pane>
        <el-tab-pane label="登录" name="signin">
          <sign-in></sign-in>
        </el-tab-pane>
      </el-tabs>
    </el-card>
  </div>
  <router-view />
</template>

<script>
import SignIn from '../components/SignIn.vue';
import SignUp from '../components/SignUp.vue';
export default {
  name: 'Login',
  components: {
    SignIn,
    SignUp,
  },
  data: function () {
    return {
      active: 'signup', // signup, signin
    };
  },
  methods: {
    handleClick: function (tab, event) {
      console.log(tab, event);
    },
  },
};
</script>

<style scoped>
#login {
  width: 100%;
  height: 100%;
  vertical-align: middle;
  text-align: center;
  background: url('../../public/bg.jpg') no-repeat;
  background-size: 100% 100%;
}
#login-card {
  width: 400px;
  height: fit-content;
  min-height: 200px;
  position: absolute;
  text-align: center;
  margin: auto;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
}
</style>
