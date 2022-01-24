<template>
  <div id="container">
    <el-menu
      id="head"
      :default-active="activeRoute"
      :router="true"
      mode="horizontal"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
    >
      <el-icon id="head-icon" size="40"><first-aid-kit /></el-icon>
      <li id="head-title">Diagnosis</li>
    </el-menu>
    <div id="content">
      <router-view />
    </div>
  </div>
</template>

<script>
import { FirstAidKit } from '@element-plus/icons';
export default {
  components: {
    FirstAidKit,
  },
};
</script>

<style>
html,
body,
#app {
  margin: 0;
  width: 100%;
  height: 100%;
  padding: 0;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  width: 100%;
  min-height: 100%;
  height: auto;
}
#container {
  width: 100%;
  min-height: 100%;
  height: auto;
}
#head {
  width: 100%;
  height: 60px;
  align-items: center;
  background: rgb(90, 89, 89);
}
#head-title {
  color: rgb(255, 255, 255);
  font-weight: 900;
  font-size: 40px;
  margin: 0 50px 0 20px;
  float: left;
}
#head-icon {
  color: rgb(255, 255, 255);
  margin-left: 20px;
}
#content {
  position: absolute;
  top: 60px;
  left: 0;
  bottom: 0;
  right: 0;
}
</style>
