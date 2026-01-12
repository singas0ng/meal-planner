<script setup lang="ts">

const props = defineProps<{
  isOpen: boolean;
  title: string;
  message: string;
  type?: 'success' | 'error';
}>();

const emit = defineEmits(['close']);

const closeModal = () => {
  emit('close');
};
</script>

<template>
  <div v-if="isOpen" class="modal-overlay" @click="closeModal">
    
    <div class="modal-content" @click.stop :class="type">
      
      <h3>{{ title }}</h3>
      
      <p>{{ message }}</p>
      
      <div class="modal-actions">
        <button @click="closeModal">OK</button>
      </div>
      
    </div>
  </div>
</template>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0; left: 0; width: 100%; height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* Dimmed background */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  width: 300px;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

/* Dynamic Styles based on type */
.modal-content.success h3 { color: #42b983; }
.modal-content.error h3 { color: #ff5252; }

.modal-actions {
  margin-top: 20px;
}

button {
  padding: 8px 16px;
  cursor: pointer;
  background-color: #ddd;
  border: none;
  border-radius: 4px;
}
</style>