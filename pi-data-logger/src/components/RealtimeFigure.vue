<template>
  <div class="realtime-figure">
    <div id="chart">
      <apexchart ref="chart" type="line" height="350" :options="chartOptions" :series="series"></apexchart>
    </div>

    <button class="btn btn-success" @click="startPiDataLogger">START</button>
    <button class="btn btn-secondary ms-1" @click="stopPiDataLogger">HALT</button>
    <button class="btn btn-danger ms-1" @click="continiousGetRecord">TEST</button>

  
  </div>
</template>

<script>
  import { apexChartConifg } from '@/assets/chartConfig/chartConfig.js'
  import moment from 'moment';
  import api from '@/api/apiManager'
  export default {
    name: 'RealtimeFigure',
    props: {
      msg: String
    },
    data() {
      return {
        series: [{
          data: []
        }],
        chartOptions: apexChartConifg.basicChartOptions,
        callibrator: null
      }
    },
    methods: {
      startPiDataLogger : async ()=>{
        let status = ""
        try {
          let res = await api.startRecord()
          status = res.data
        } catch (error) {
          console.log("start fail: ", error)
        } finally {
          if(status){
            // 呼叫持續更新函式
            // this.getCurrentRecord()
          }
        }
      },
      stopPiDataLogger : async ()=>{
        let result = ""
        try {
          let res = await api.stopRecord()
          result = res.data
        } catch (error) {
          console.log("stop logger fail: ", error)
        } finally {
          if(result){
            console.log(result)
          }
        }
      },
      getNewestRecord: async ()=>{
        try {
          let res = await api.getRecordData()
          return res.data || []
        } catch (error) {
          console.log(error)
        }
      },
      continiousGetRecord(){
        this.callibrator = setInterval( async ()=>{
          let newData = await this.getNewestRecord()
          let parseData = []
          let parseLabel = []
          newData.forEach(element => {
            parseLabel.push(element.DATE)
            parseData.push(element.TEMP)
          });

          this.updateData(parseData, parseLabel)
        }, 1000)
      },
      generateData() {
        let value, label
        label = moment().format("HH:mm:ss")
        function getRndInteger(min, max) {
          return Math.floor(Math.random() * (max - min + 1)) + min
        }
        value = getRndInteger(20, 120)
        return { label, value }
      },
      updateData(dataArray, labelArray) {
        this.$refs.chart.updateSeries([{
          data: dataArray
        }])
        this.$refs.chart.updateOptions({
          xaxis: {
            categories: labelArray
          }
        })
      },
      initFetch() {
        this.callibrator = setInterval(() => {
          let newData = []
          for (let i = 0; i < 10; i++) {
            newData.push( this.generateData() )
          }

          let dataArray=[], labelArray=[]
          for (let i = 0; i < 10; i++) {
            dataArray.push(newData[i].value)
            labelArray.push(newData[i].label)
          }

          this.updateData(dataArray, labelArray)
        }, 1000)

      },
      stopFetch() {
        clearInterval(this.callibrator)
      }
    },
    mounted() {
      this.chartOptions.title.text = "DEMO CHART"
    }
  }
</script>

<style scoped>
</style>