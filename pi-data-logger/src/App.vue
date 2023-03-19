<template>
  <RealtimeFigure />
  <!-- <HelloWorld msg="Welcome to Your Vue.js App" /> -->

  <!-- <button type="button" class="btn btn-primary" @click="getVersion">11111</button>
  <button type="button" class="btn btn-primary" @click="getVersionAPI">22222</button>
  <div class="card" style="width: 18rem;">
    <h5><span class="badge bg-secondary"> VERSION</span> {{version}}</h5>
    <p>{{allResponse}}</p>
  </div> -->
</template>

<script>
  // import HelloWorld from './components/HelloWorld.vue'
  import RealtimeFigure from './components/RealtimeFigure.vue'
  import axios from 'axios'
  import api from '@/api/apiManager'
  export default {
    name: 'App',
    components: {
      // HelloWorld,
      RealtimeFigure
    },
    data() {
      return {
        version: "N/A",
        allResponse: null
      }
    },
    methods: {
      getVersion() {
        axios({
          method: 'get',
          url: 'http://127.0.0.1:5000/version',
        })
          .then((response) => {
            this.allResponse = response
            this.version = response.data
          });

      },

      getVersionAPI: async () => {
        // 呼叫API
        try {
          let res = await api.getVersion();

          console.log(res);
        } catch (error) {
          console.log(error);
        }
      }
    }
  }
</script>

<style lang="scss">
  
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>