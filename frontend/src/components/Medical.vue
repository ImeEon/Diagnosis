<template>
  <el-scrollbar height="100%">
    <el-card shadow="hover" class="health-card">
      <h3>点击上传</h3>
      <el-upload
        :action="$store.getters.URL_SET_MEDICAL_IMAGES"
        :headers="{ username: $store.getters.username }"
        :name="$store.getters.username"
        :on-success="uploadSuccess"
        list-type="picture-card"
        multiple="false"
        :show-file-list="false"
      >
        <el-icon><Plus /></el-icon>
        <template #tip>
          <div class="el-upload__tip">文件名不含中文</div>
        </template>
      </el-upload>
      <el-dialog v-model="dialogVisible">
        <img width="100%" :src="dialogImageUrl" alt="" />
      </el-dialog>
      <h3>已经上传</h3>
      <el-scrollbar min-height="50px">
        <el-image
          class="upload"
          v-for="(upload, index) in uploadList"
          v-bind:key="index"
          :src="upload"
          :preview-src-list="[upload]"
        ></el-image>
      </el-scrollbar>
      <h3>处理结果</h3>
      <el-scrollbar min-height="50px">
        <el-image
          class="result"
          v-for="(result, index) in resultList"
          v-bind:key="index"
          :src="result"
          :preview-src-list="[result]"
        ></el-image>
      </el-scrollbar>
    </el-card>
  </el-scrollbar>
</template>

<script>
import { Plus } from '@element-plus/icons';
import { ElMessage } from 'element-plus';
import axios from 'axios';
export default {
  name: 'Medical',
  data() {
    return {
      dialogVisible: false,
      uploadList: [],
      resultList: [],
    };
  },
  components: {
    Plus,
  },
  mounted: function () {
    this.getUploadAndResult();
  },
  methods: {
    getUploadAndResult() {
      const that = this;
      axios
        .post(that.$store.getters.URL_GET_MEDICAL_IMAGES, {
          username: that.$store.getters.username,
        })
        .then(function (response) {
          if (response.data.flag === true) {
            console.log(response);
            that.uploadList = response.data.upload.map(
              (d) => that.$store.getters.MEDICAL_IMAGE_BASE + d,
            );
            that.resultList = response.data.result.map(
              (d) => that.$store.getters.MEDICAL_IMAGE_BASE + d,
            );
          } else {
            ElMessage.warning('暂无图片');
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    uploadSuccess(response) {
      console.log(response);
      if (response.flag === true) {
        ElMessage.success('上传成功');
        this.uploadList.push(
          this.$store.getters.MEDICAL_IMAGE_BASE + response.upload,
        );
        this.resultList.push(
          this.$store.getters.MEDICAL_IMAGE_BASE + response.result,
        );
      } else {
        ElMessage.error('上传失败');
      }
    },
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url;
      this.dialogVisible = true;
    },
  },
};
</script>

<style scoped>
.health-card {
  width: auto;
  height: 100%;
  padding: 20px;
}
.upload,
.result {
  width: 148px;
  height: 148px;
  margin: 5px;
  border-radius: 4px;
}
</style>
