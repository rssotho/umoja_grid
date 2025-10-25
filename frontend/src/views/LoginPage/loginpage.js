export default {
  name: 'LoginPage',
  data() {
    return {
      form: {
        email: '',
        password: '',
        remember: false
      }
    }
  },
  methods: {
    handleLogin() {
      console.log('Login submitted:', this.form);
      alert(`Login successful!\nEmail: ${this.form.email}`);
      // Add your login API call here
    }
  }
}