<template>
    <div>
        <BarChart :key="chartKey" :data="chartData" :options="chartOptions" />
    </div>
  </template>
  
  <script>
  import { Bar } from 'vue-chartjs';
  import { Chart, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';
  import axios from 'axios';
  
  // Register the necessary components with Chart.js
  Chart.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);
  
  export default {
    components: {
      BarChart: Bar
    },
    data() {
      return {
        chartData: {
          labels: [],
          datasets: [
            {
              label: 'Total Sales',
              backgroundColor: '#42A5F5',
              data: []
            },
            {
              label: 'Total Invoices',
              backgroundColor: '#66BB6A',
              data: []
            }
          ]
        },
        chartOptions: {
      responsive: true,
      maintainAspectRatio: false
    },
    chartKey: 0
      };
    },
    async created() {
      await this.fetchData();
    },
    methods: {
      async fetchData() {
        try {
          const salesResponse = await axios.get('http://localhost:8000/api/sales/', {
            headers: {
              Authorization: `Bearer ${localStorage.getItem('token')}`
            }
          });
          const invoicesResponse = await axios.get('http://localhost:8000/api/invoices/', {
            headers: {
              Authorization: `Bearer ${localStorage.getItem('token')}`
            }
          });
  
          // Extract and aggregate data
          const salesData = this.aggregateSalesData(salesResponse.data.sales_data);
          const invoicesData = this.aggregateInvoiceData(invoicesResponse.data);
          console.log("salesData",Object.values(salesData))
          console.log("invoicesData",Object.values(invoicesData))
          // Set labels and data
          this.chartData.labels = Object.keys(salesData); // Dates
          this.chartData.datasets[0].data = Object.values(salesData); // Sales amounts
          this.chartData.datasets[1].data = Object.values(invoicesData); // Invoice quantities
          console.log("Updated Chart Data:", this.chartData);
          this.chartKey += 1;
        } catch (error) {
          console.error("Error fetching data:", error);
        }
      },
      aggregateSalesData(salesData) {
        return salesData.reduce((acc, item) => {
          const date = item.date.substring(0, 10);
          const saleAmount = parseFloat(item.sale_amount);
          if (!acc[date]) {
            acc[date] = 0;
          }
          acc[date] += saleAmount;
          return acc;
        }, {});
      },
      aggregateInvoiceData(invoicesData) {
        return invoicesData.reduce((acc, item) => {
          const date = item.date.substring(0, 10);
          const quantity = item.quantity;
          if (!acc[date]) {
            acc[date] = 0;
          }
          acc[date] += quantity;
          return acc;
        }, {});
      }
    }
  };
  </script>
  