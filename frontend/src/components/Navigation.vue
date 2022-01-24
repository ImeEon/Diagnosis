<template>
  <div id="menu">
    <el-menu class="el-menu-vertical-demo" :uniqueOpened="true" :router="true">
      <el-menu-item :index="nav.info.url">
        <el-icon><avatar /></el-icon>
        <template #title>{{ nav.info.title }}</template>
      </el-menu-item>
      <el-menu-item :index="nav.medical.url">
        <el-icon><copy-document /></el-icon>
        <template #title>{{ nav.medical.title }}</template>
      </el-menu-item>
      <el-menu-item :index="nav.list.url">
        <el-icon><first-aid-kit /></el-icon>
        <template #title>{{ nav.list.title }}</template>
      </el-menu-item>
      <el-menu-item :index="nav.date.url">
        <el-icon><alarm-clock /></el-icon>
        <template #title>{{ nav.date.title }}</template>
      </el-menu-item>
      <el-menu-item :index="nav.log.url">
        <el-icon><chat-line-square /></el-icon>
        <template #title>{{ nav.log.title }}</template>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
import {
  CopyDocument,
  Avatar,
  FirstAidKit,
  AlarmClock,
  ChatLineSquare,
} from '@element-plus/icons';
export default {
  name: 'Navigation',
  components: {
    CopyDocument,
    Avatar,
    FirstAidKit,
    AlarmClock,
    ChatLineSquare,
  },
  computed: {
    nav: function () {
      if (this.$store.getters.usertype === 'doctor') {
        return {
          info: { url: '/doctorinfo', title: '个人信息' },
          medical: { url: '/todo', title: '医疗模块' },
          list: { url: '/todo', title: '患者信息' },
          date: { url: '/todo', title: '患者预约' },
          log: { url: '/todo', title: '患者留言' },
        };
      } else {
        return {
          info: { url: '/patientinfo', title: '个人信息' },
          medical: { url: '/medical', title: '医疗模块' },
          list: { url: '/doctors', title: '医生信息' },
          date: { url: '/todo', title: '我的预约' },
          log: { url: '/todo', title: '我的留言' },
        };
      }
    },
  },
};
</script>

<style scoped>
#menu {
  width: 100%;
  height: auto;
}
</style>
