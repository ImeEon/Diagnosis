import { createRouter, createWebHistory } from 'vue-router';
import Login from '../views/Login.vue';
import Main from '../views/Main.vue';
import PatientInfo from '../components/PatientInfo.vue';
import DoctorInfo from '../components/DoctorInfo.vue';
import Doctors from '../components/Doctors.vue';
import Medical from '../components/Medical.vue';
import Todo from '../components/Todo.vue';

const routes = [
  {
    path: '/',
    redirect: '/login',
  },
  {
    path: '/login',
    component: Login,
  },
  {
    path: '/main',
    component: Main,
    children: [
      {
        path: '/patientinfo',
        component: PatientInfo,
      },
      {
        path: '/doctorinfo',
        component: DoctorInfo,
      },
      {
        path: '/medical',
        component: Medical,
      },
      {
        path: '/doctors',
        component: Doctors,
      },
      {
        path: '/todo',
        component: Todo,
      },
    ],
  },
];

export default createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});
