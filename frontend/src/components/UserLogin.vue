<template>
  <v-container
    fluid
    class="login-container"
    fill-height
  >
    <v-row
      align="center"
      justify="center"
      
    >
      <v-col cols="12" sm="8" md="4" justify="end">
        <v-card class="pa-5 login-card" justify="end">
          <v-card-title class="text-center">Login</v-card-title>
          <v-card-text>
            <v-form @submit.prevent="login">
              <v-text-field
                v-model="username"
                label="Username"
                outlined
                required
              ></v-text-field>
              <v-text-field
                v-model="password"
                label="Password"
                type="password"
                outlined
                required
              ></v-text-field>
              <v-btn
                color="primary"
                type="submit"
                block 
                style="background-color: #008af3;"
              >
                Login
              </v-btn>
            </v-form>
            <div v-if="error" class="error-message">{{ error }}</div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        password: '',
        error: null,
      };
    },
    methods: {
      async login() {
        try {
          const response = await axios.post('http://localhost:8000/api/token/', {
            username: this.username,
            password: this.password
          });

          // Store the access token (and optionally refresh token) in localStorage
          localStorage.setItem('access_token', response.data.access);
          localStorage.setItem('refresh_token', response.data.refresh);
          localStorage.setItem('token', response.data.access);


          // Redirect to the dashboard
          // router.push({path:"/dashboard"})
          this.$router.push({path:"/dashboard"});
        } catch (err) {
            console.log(err)
          this.error = 'Invalid credentials';
        }
      }
    }
  };
  </script>
  <style scoped>
  /* Background image and centering */
  .login-container {
    background-image: url('../../public/cover.png'); /* Replace with your image URL */
    background-size: cover;
    background-position: center;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .login-card {
    opacity: 0.95;
    background-color: rgba(255, 255, 255, 0.85); /* Slight transparency for better background effect */
    border-radius: 8px;
  }
  
  /* Error message styling */
  .error-message {
    color: red;
    margin-top: 10px;
    font-size: 14px;
    text-align: center;
  }
  </style>