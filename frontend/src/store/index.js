import { createStore } from 'vuex';

export default createStore({
  state: {
    API_BASE: '//127.0.0.1:5005',
    AVATER_IMAGE_BASE: '//127.0.0.1:5005/data/images/avatars/',
    MEDICAL_IMAGE_BASE: '//127.0.0.1:5005/data/images/medical/',
    username: '',
    usertype: '',
  },
  mutations: {
    setUsername(state, username) {
      state.username = username;
    },
    setUsertype(state, usertype) {
      state.usertype = usertype;
    },
  },
  actions: {},
  modules: {},
  getters: {
    URL_TEST: (state) => state.API_BASE + '/api/test',
    URL_SIGNUP: (state) => state.API_BASE + '/api/signup',
    URL_SIGNIN: (state) => state.API_BASE + '/api/signin',
    URL_GET_USERTYPE: (state) => state.API_BASE + '/api/getusertype',
    URL_SET_PATIENT_INFO: (state) => state.API_BASE + '/api/setpatientinfo',
    URL_GET_PATIENT_INFO: (state) => state.API_BASE + '/api/getpatientinfo',
    URL_SET_DOCTOR_INFO: (state) => state.API_BASE + '/api/setdoctorinfo',
    URL_GET_DOCTOR_INFO: (state) => state.API_BASE + '/api/getdoctorinfo',
    URL_GET_AVATAR: (state) => state.API_BASE + '/api/getavatar',
    URL_SET_AVATAR: (state) => state.API_BASE + '/api/setavatar',
    URL_SET_MEDICAL_IMAGES: (state) => state.API_BASE + '/api/setmedicalimage',
    URL_GET_MEDICAL_IMAGES: (state) => state.API_BASE + '/api/getmedicalimages',
    URL_GET_ALL_DOCTOR_USERNAME: (state) =>
      state.API_BASE + '/api/getalldoctorusername',

    username: (state) => state.username,
    usertype: (state) => state.usertype,

    API_BASE: (state) => state.API_BASE,
    AVATER_IMAGE_BASE: (state) => state.AVATER_IMAGE_BASE,
    MEDICAL_IMAGE_BASE: (state) => state.MEDICAL_IMAGE_BASE,
  },
});
