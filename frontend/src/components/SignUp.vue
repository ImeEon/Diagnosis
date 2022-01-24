<template>
  <div id="signup">
    <el-form
      :model="ruleForm"
      status-icon
      :rules="rules"
      ref="ruleForm"
      label-width="80px"
    >
      <el-form-item label="类型" prop="usertype">
        <el-select
          v-model="ruleForm.usertype"
          placeholder="请选择"
          style="width: 240px"
        >
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          ></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="用户名" prop="username">
        <el-input
          type="string"
          v-model="ruleForm.username"
          autocomplete="off"
        ></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input
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
  name: 'SignUp',
  data() {
    var validateUsertype = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请选择用户类型'));
      } else {
        callback();
      }
    };
    var validateUsername = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入用户名'));
      } else {
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
        usertype: '',
        username: '',
        password: '',
      },
      rules: {
        usertype: [{ validator: validateUsertype, trigger: 'blur' }],
        username: [{ validator: validateUsername, trigger: 'blur' }],
        password: [{ validator: validatePassword, trigger: 'blur' }],
      },
      options: [
        {
          value: 'patient',
          label: '患者',
        },
        {
          value: 'doctor',
          label: '医生',
        },
      ],
    };
  },
  methods: {
    submitForm(formName) {
      const that = this;
      that.$refs[formName].validate((valid) => {
        if (valid) {
          that.signUp();
        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },
    signUp() {
      const that = this;
      axios
        .post(that.$store.getters.URL_SIGNUP, {
          usertype: that.ruleForm.usertype,
          username: that.ruleForm.username,
          password: that.ruleForm.password,
        })
        .then(function (response) {
          console.log(response);
          if (response.data.flag === true) {
            ElMessage.success('注册成功!');
            that.$store.commit('setUsername', that.ruleForm.username);
            that.goToMain();
          } else {
            ElMessage.error('注册失败，用户名已存在');
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
