export default {
  name: 'ForgotPasswordPage',
  data() {
    return {
      email: ''
    }
  },
  methods: {
    handleForgotPassword() {
      console.log('Reset link requested for:', this.email);
      alert(`If an account exists for ${this.email}, a reset link will be sent.`);
      // Add your API call to request password reset here
    }
  }
}