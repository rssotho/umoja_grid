<template>
  <div class="position-relative min-vh-100">
    <!-- Video Background -->
    <video autoplay muted loop playsinline class="position-fixed top-0 start-0 w-100 h-100 video-bg object-fit-cover">
      <source src="@/assets/videos/hero.webm" type="video/webm">
    </video>
    
    <!-- Dark Overlay -->
    <div class="position-fixed top-0 start-0 w-100 h-100 bg-dark bg-opacity-50"></div>
    
    <div class="container-fluid min-vh-100 d-flex align-items-center justify-content-center py-5">
      <div class="row w-100 justify-content-center">
      <div class="col-12 col-md-10 col-lg-8 col-xl-6">
        
        <div class="card border-0 shadow-lg rounded-5 overflow-hidden bg-white bg-opacity-95">
          <div class="row g-0">
            <!-- Left Side - Branding -->
            <div class="col-md-5 bg-dark text-white d-none d-md-flex flex-column justify-content-center align-items-center p-5">
              <div class="text-center">
                <img src="@/assets/brand.png" alt="Logo" class="mb-4 rounded-3 img-fluid logo-brand object-fit-cover">
                <h1 class="small fw-bold mb-3">Welcome Back!</h1>
                <p class="mb-4 small">Sign in to continue your journey with us</p>
                <div class="border-top border-secondary pt-4">
                  <p class="mb-3 small">New here?</p>
                  <router-link to="/signup" class="btn btn-outline-light btn-lg px-4 button rounded-4 py-2">Sign up</router-link>
                </div>
              </div>
            </div>
            
            <!-- Right Side - Login Form -->
            <div class="col-md-7">
              <div class="card-body px-4 py-5 px-md-5 py-md-5 px-lg-5 py-lg-5">
                <h1 class="fw-bold mb-2 fs-4">Sign In</h1>
                <p class="text-muted mb-4 small">Enter your credentials to access your account</p>
                
                <form @submit.prevent="handleLogin">
                  <div class="mb-2">
                    <label class="form-label fw-medium small">Email Address</label>
                    <input 
                      v-model="form.email" 
                      type="email" 
                      class="form-control form-control-lg rounded-4" 
                      placeholder="name@example.com" 
                      required
                    >
                  </div>
                  
                  <div class="mb-3">
                    <label class="form-label fw-medium small">Password</label>
                    <input 
                      v-model="form.password" 
                      type="password" 
                      class="form-control form-control-lg rounded-4" 
                      placeholder="Enter your password" 
                      required
                    >
                  </div>
                  
                  <div class="d-flex justify-content-between align-items-center mb-4">
                    <div class="form-check">
                      <input 
                        v-model="form.remember" 
                        type="checkbox" 
                        class="form-check-input" 
                        id="rememberMe"
                      >
                      <label class="form-check-label small" for="rememberMe">Remember me</label>
                    </div>
                    <router-link to="/forgotpassword" class="text-decoration-none text-dark fw-semibold small">
                      Forgot Password?
                    </router-link>
                  </div>
                  
                  <button type="submit" class="btn btn-dark btn-lg w-100 rounded-4 py-2 fw-semibold button">
                    Sign In
                  </button>
                  
                  <div class="d-md-none text-center mt-4">
                    <p class="text-muted mb-2 small">Don't have an account?</p>
                    <router-link to="/signup" class="text-dark fw-semibold text-decoration-none">
                      Create Account
                    </router-link>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
        
      </div>
    </div>
  </div>
  </div>
</template>
<script src="./loginpage.js"></script>
<style src="./loginpage.css"></style>