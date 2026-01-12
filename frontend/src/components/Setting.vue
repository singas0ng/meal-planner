<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';
import BaseModal from '../components/BaseModal.vue';

const isLoading = ref(false);

const showModal = ref(false);
const modalTitle = ref('');
const modalMessage = ref('');
const modalType = ref<'success' | 'error'>('success');

const resetSetting = ref({
  autoReset: false,
  resetInterval: 7,
});


const notifySetting = ref({
  autoReset: false,
  resetInterval: 7,
});

const saveAllSettings = async () => {
  isLoading.value = true;

  try {
    await axios.put('http://localhost:8000/reset', resetSetting.value);
    await axios.put('http://localhost:8000/notify', notifySetting.value);
    
    modalTitle.value = "Success!";
    modalMessage.value = "Your settings have been updated.";
    modalType.value = "success";
    showModal.value = true;

  } catch (error) {
    modalTitle.value = "Error";
    modalMessage.value = "Failed to connect to the server.";
    modalType.value = "error";
    showModal.value = true;
  } finally {
    isLoading.value = false;
  }
};
</script>

<template>
  <div class="settings-container">
    <h1>Settings</h1>
    
    <div class="card">

    </div>

    <button @click="saveAllSettings" :disabled="isLoading" class="save-btn">
      {{ isLoading ? 'Saving...' : 'Save Changes' }}
    </button>

    <BaseModal 
      :is-open="showModal" 
      :title="modalTitle" 
      :message="modalMessage" 
      :type="modalType"
      @close="showModal = false"
    />
    
  </div>
</template>