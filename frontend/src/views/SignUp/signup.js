export default {
  name: 'SignUp',
  data() {
    return {
      form: {
        name: '',
        email: '',
        password: '',
        confirmPassword: '',
        terms: false
      }
    }
  },
  methods: {
    handleSignup() {
      if (this.form.password !== this.form.confirmPassword) {
        alert("Passwords do not match!");
        return;
      }
      console.log('Signup submitted:', this.form);
      alert(`Signup successful!\nName: ${this.form.name}\nEmail: ${this.form.email}`);
      // Add your signup API call here
    }
  }
}