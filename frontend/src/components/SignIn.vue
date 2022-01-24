<template>
  <div>
    <el-form
      :model="ruleForm"
      status-icon
      :rules="rules"
      ref="ruleForm"
      label-width="80px"
    >
      <el-form-item label="用户名" prop="username">
        <el-input
          type="string"
          v-model="ruleForm.username"
          autocomplete="off"
        ></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input
          show-password="true"
          type="password"
          v-model="ruleForm.password"
          autocomplete="off"
        ></el-input>
      </el-form-item>
    </el-form>
    <el-button
      id="commit-button"
      type="primary"
      @click="submitForm('ruleForm')"
    >
      提交
    </el-button>
  </div>
</template>

<script>
import axios from 'axios';
import { ElMessage } from 'element-plus';
export default {
  name: 'SignIn',
  data() {
    var validateUsername = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入用户名'));
      } else {
        if (this.ruleForm.checkPass !== '') {
          this.$refs.ruleForm.validateField('checkPass');
        }
        callback();
      }
    };
    var validatePassword = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'));
      } else {
        callback();
      }
    };
    return {
      ruleForm: {
        username: '',
        password: '',
      },
      rules: {
        username: [{ validator: validateUsername, trigger: 'blur' }],
        password: [{ validator: validatePassword, trigger: 'blur' }],
      },
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.signIn();
        } else {
          return false;
        }
      });
    },
    signIn() {
      const that = this;
      axios
        .post(that.$store.getters.URL_SIGNIN, {
          username: that.ruleForm.username,
          password: that.ruleForm.password,
        })
        .then(function (response) {
          if (response.data.flag === true) {
            ElMessage.success('登录成功!');
            that.$store.commit('setUsername', that.ruleForm.username);
            that.goToMain();
          } else {
            ElMessage.error('登录失败，用户名或密码错误');
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    goToMain() {
      this.$router.push('/main');
    },
  },
};
</script>

<style scoped>
#commit-button {
  width: 100px;
}
.el-input {
  width: 240px;
}
</style>
