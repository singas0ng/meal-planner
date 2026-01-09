<script setup lang="ts">
import { ref, onMounted } from 'vue'

  // variable that hold the message
  const message = ref('Waiting for connection with backend...')

  // Define a function to fetch data
  const getMessage = async () => {
    try {
      // Ask the Python backend for data
      const response = await fetch('http://127.0.0.1:8000/api/message')
      const data = await response.json()

      // Update our variable with the message from Python
      message.value = data.message
    } catch (error) {
      console.error('Error fetching data:', error)
      message.value = 'Failed to connect to backend :('
    }
  }

  // run function automatically when the page loads
  onMounted(() => {
    getMessage()
  })

</script>

<template>
  <div class="container">
    <h1>Meal Planner 🍱</h1>
    <p>Message from Python:</p>
    <h2 class="backend-msg">{{ message }}</h2>
  </div>
</template>

<style scoped>
.container {
  text-align: center;
  margin-top: 50px;
  font-family: Arial, sans-serif;
}
.backend-msg {
  color: #42b883;
  font-weight: bold;
}
</style>
