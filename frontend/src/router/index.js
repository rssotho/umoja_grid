import { createRouter, createWebHistory } from "vue-router"
import CryptoJS from "crypto-js"

// VIEWS
import LoginPage from "@/views/LoginPage/LoginPage.vue";
import SignUp from "@/views/SignUp/SignUp.vue";
import ForgotPassword from "@/views/ForgotPassword/ForgotPassword.vue";

// --- ROUTES MUST BE BEFORE createRouter ---
const routes = [
  { path: "/", name: "LoginPage", component: LoginPage },
  { path: "/signup", name: "SignUp", component: SignUp },
  { path: "/forgotpassword", name: "ForgotPassword", component: ForgotPassword },
]

const encryption_key = process.env.VUE_APP_ENCRYPTION_KEY

export function set_token(token) {
  var encrypted_token = CryptoJS.AES.encrypt(token, encryption_key).toString()
  localStorage.setItem("encrypted_token", encrypted_token)
}

export function get_token() {
  var encrypted_token = localStorage.getItem("encrypted_token")
  if (encrypted_token) {
    var decrypted_token = CryptoJS.AES.decrypt(encrypted_token, encryption_key)
    return decrypted_token.toString(CryptoJS.enc.Utf8)
  }
  return null
}

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  var token = localStorage.getItem("encrypted_token")
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    token ? next() : next("/")
  } else {
    next()
  }
})

export function clear_token() {
  localStorage.removeItem("encrypted_token")
}

export function set_user_details(user_details) {
  localStorage.setItem("role", user_details.role)
  localStorage.setItem("user_id", user_details.user_id)
  localStorage.setItem("last_name", user_details.last_name)
  localStorage.setItem("first_name", user_details.first_name)
}

export function get_user_details() {
  return {
    role: localStorage.getItem("role"),
    user_id: localStorage.getItem("user_id"),
    last_name: localStorage.getItem("last_name"),
    first_name: localStorage.getItem("first_name"),
  }
}

export default router
