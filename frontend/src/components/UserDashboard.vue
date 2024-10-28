<template>
  <div class="container mt-5">
    
    <div class="container">
    <h2 class="mt-4 mb-4">Product Filters</h2>
    <form class="mb-4">
      <div class="row">
        <div class="col-md-4 mb-3">
          <input 
            type="text" 
            v-model="filters.store_name" 
            @input="applyFilters" 
            class="form-control" 
            placeholder="Store Name" 
          />
        </div>
        <div class="col-md-4 mb-3">
          <input 
            type="text" 
            v-model="filters.category" 
            @input="applyFilters" 
            class="form-control" 
            placeholder="Category" 
          />
        </div>
        <div class="col-md-4 mb-3">
          <input 
            type="text" 
            v-model="filters.vendor_name" 
            @input="applyFilters" 
            class="form-control" 
            placeholder="Vendor Name" 
          />
        </div>
      </div>
      <div class="row">
        
        <div class="col-md-4 mb-3">
          <input 
            type="text" 
            v-model="filters.item_number" 
            @input="applyFilters" 
            class="form-control" 
            placeholder="Item Number" 
          />
        </div>
        <div class="col-md-4 mb-3">
          <input 
            type="text" 
            v-model="filters.name" 
            @input="applyFilters" 
            class="form-control" 
            placeholder="Product Name" 
          />
        </div>
      </div>
    </form>
    </div>
    <h1 class="text-center mb-4">Product List</h1>
    <button @click="fetchData" class="btn btn-primary mb-3">Refresh Data</button>
    <div v-if="loading" class="alert alert-info">Loading...</div>
    <div v-if="error" class="alert alert-danger">{{ error }}</div>

    <div>
    <v-data-table
      :headers="headers"
      :items="filteredProducts"
      :loading="loading"
      :items-per-page="50"
      class="elevation-1"
      :search="search"
      show-select
      
    >
      <template v-slot:top>
        <v-text-field
          v-model="search"
          label="Search products"
          clearable
          @input="filterProducts"
        ></v-text-field>
      </template>

      <template v-slot:body-cell="{ item }">
        <span>${{ item.sale_dollars }}</span>
      </template> 

      <template v-slot:no-data>
        <v-alert type="info" icon="mdi-information">
          No products available.
        </v-alert>
      </template>
    </v-data-table>
    
  </div>
  <div>
    <h4> Sales And Profit Chart</h4>
    <SalesInvoiceChart />
  </div> 
  </div>
  
  

</template>

<script>
import axios from 'axios';
import SalesInvoiceChart from './SalesInvoiceChart.vue';
export default {
  components: {
    SalesInvoiceChart
  },
  data() {
    return {
      filters: {
        store_name: '',
        city: '',
        zip_code: '',
        category: '',
        vendor_name: '',
        item_number: '',
        pagination: {
          page: 1,
          rowsPerPage: 50,
        },
      },
      products: [],
      loading: false,
      error: null,
      filteredProducts: [],
      search: '',
      headers: [
        { text: 'Item Number', value: 'item_number' },
        { text: 'Product Desc', value: 'item_desc' },
        { text: 'Category', value: 'category' },
        { text: 'Sale Dollars', value: 'sale_dollars' },
        { text: 'State Bottle Cost', value: 'state_bottle_cost' },
        { text: 'State Bottle Retail', value: 'state_bottle_retail' },
        { text: 'Store Number', value: 'store_number' },
        { text: 'Store Address', value: 'address' },
        { text: 'Vendor Number', value: 'vendor_number' },
        { text: 'County', value: 'county' },
        { text: 'County Number', value: 'county_number' },
        { text: 'Date', value: 'date' },
        { text: 'Invoice Item Number', value: 'invoice_item_number' },
        { text: 'Zip Code', value: 'zip_code' },
      ],
    };
  },
  async mounted() {
    await this.fetchData();
  },
  methods: {
  async fetchData() {
    this.loading = true;
    this.error = null; // Reset error before fetching
    try {
        const response = await axios.get('http://localhost:8000/api/products/', {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`
          }
        });

        console.log("Response Data:", response.data); 
        this.products = response.data; 
        this.filteredProducts = response.data;
      } catch (err) {
        console.error("Error:", err); 
        console.error("response:", err.response); 
        if (err.response && err.response.data) {
          const errorMessage = err.response.data.code;
          console.log(errorMessage)
          if (errorMessage === "token_not_valid") {
            
            localStorage.removeItem('token'); 
            window.location.href = '/login';
            // this.$router.push({path:"/login"});
           
          }
        }
        this.error = 'Error fetching data'; 
      } finally {
        this.loading = false;
      }

  },
  applyFilters() {
      // console.log((this.filters.store_name);
      this.filteredProducts = this.products.filter(product => {
        return (
          (this.filters.store_name ? product.store_name.toLowerCase().includes(this.filters.store_name.toLowerCase()) : true) &&
          (this.filters.name ? product.name.toLowerCase().includes(this.filters.name.toLowerCase()) : true) &&
          (this.filters.zip_code ? product.zip_code === this.filters.zip_code : true) &&
          (this.filters.category ? product.category_name.toLowerCase().includes(this.filters.category.toLowerCase()) : true) &&
          (this.filters.vendor_number ? product.vendor_number.toLowerCase().includes(this.filters.vendor_name.toLowerCase()) : true) &&
          (this.filters.item_number ? product.item_number.toLowerCase().includes(this.filters.item_number.toLowerCase()) : true)
        );
      });
    },
    filterProducts() {
      const searchTerm = this.search.toLowerCase();
      this.filteredProducts = this.products.filter(
        (product) =>
          product.item_desc?.toLowerCase().includes(searchTerm) ||
          product.category?.toLowerCase().includes(searchTerm) ||
          product.vendor_number?.toLowerCase().includes(searchTerm) ||
          product.category?.toLowerCase().includes(searchTerm) ||
          product.store_number?.toString().includes(searchTerm)
      );
    },
}

};
</script>

<style scoped>
.v-data-footer__icons-before, .v-data-footer__icons-after {
  opacity: 1 !important; /* Ensure the button is visible */
}

.v-btn {
  background-color: #3f51b5 !important; /* Use your preferred color */
  color: white !important; /* Text color */
}
</style>
