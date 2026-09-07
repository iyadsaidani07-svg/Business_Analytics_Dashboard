const uploadButton = document.getElementById("upload-button");
const fileInput = document.getElementById("file-input");
const totalRevenue = document.getElementById("total-revenue");
const totalTransactions = document.getElementById("total-transactions");
const totalQuantity = document.getElementById("total-quantity");
const averageTransaction = document.getElementById("average-transaction");
const grossRevenue=document.getElementById("gross-revenue")
//CHARTS FUNCTIONS PART
const revenueCategoryChart = document.getElementById("revenue-category-chart");
function createRevenueCategoryChart(data) {
    const categories = Object.keys(data.analytics.revenue_by_category);
    const revenues = Object.values(data.analytics.revenue_by_category);
    new Chart(revenueCategoryChart, {
        type: "bar",
        data: {
            labels: categories,

            datasets: [{
                label: "Revenue by Category",
                data: revenues
            }]
        },
        options: {
            responsive: true
        }
    });
}
const transactionsCategoryChart = document.getElementById("transactions-category-chart");
function createTransactionsCategoryChart(data) {
    const categories = Object.keys(data.analytics.transactions_per_category);
    const transactions = Object.values(data.analytics.transactions_per_category);
    new Chart(transactionsCategoryChart, {
        type: "bar",
        data: {
            labels: categories,

            datasets: [{
                label: "Transactions per Category",
                data: transactions
            }]
        },
        options: {
            responsive: true
        }
    });
}
const topCategoriesChart = document.getElementById("top-categories-chart");
function createTopCategoriesChart(data) {
    const categories = Object.keys(data.analytics.top_5_categories);
    const revenues = Object.values(data.analytics.top_5_categories);
    new Chart(topCategoriesChart, {
        type: "bar",
        data: {
            labels: categories,
            datasets: [{
                label: "Top 5 Categories",
                data: revenues
            }]
        },
        options: {
            responsive: true
        }
    });
}
const quantityCategoryChart = document.getElementById("quantity-category-chart");
function createQuantityCategoryChart(data) {
    const categories = Object.keys(data.analytics.quantity_sold_by_category);
    const quantities = Object.values(data.analytics.quantity_sold_by_category);
    new Chart(quantityCategoryChart, {
        type: "bar",
        data: {
            labels: categories,
            datasets: [{
                label: "Quantity Sold",
                data: quantities
            }]
        },
        options: {
            responsive: true
        }
    });
}
const revenueRegionChart = document.getElementById("revenue-region-chart");
function createRevenueRegionChart(data) {
    const regions = Object.keys(data.analytics.revenue_by_region);
    const revenues = Object.values(data.analytics.revenue_by_region);
    new Chart(revenueRegionChart, {
        type: "bar",
        data: {
            labels: regions,
            datasets: [{
                label: "Revenue by Region",
                data: revenues
            }]
        },
        options: {
            responsive: true
        }
    });
}
const revenueYearChart = document.getElementById("revenue-year-chart");
function createRevenueYearChart(data) {
    const years = Object.keys(data.analytics.revenue_by_year);
    const revenues = Object.values(data.analytics.revenue_by_year);
    new Chart(revenueYearChart, {
        type: "line",
        data: {
            labels: years,
            datasets: [{
                label: "Revenue by Year",
                data: revenues
            }]
        },
        options: {
            responsive: true
        }
    });
}
const revenueMonthChart = document.getElementById("revenue-month-chart");
function createRevenueMonthChart(data) {
    const months = Object.keys(data.analytics.revenue_by_month);
    const revenues = Object.values(data.analytics.revenue_by_month);
    new Chart(revenueMonthChart, {
        type: "line",
        data: {
            labels: months,
            datasets: [{
                label: "Revenue by Month",
                data: revenues
            }]
        },
        options: {
            responsive: true
        }
    });
}


//THIS IS THE MAIN FUNCTION WHICH USES ALL CONT AND FUNCTIONS ABOVE 
uploadButton.addEventListener("click", async function() {
    const file = fileInput.files[0];
    if (!file) {
        console.log("No file selected");
        return;
    }
    const formData = new FormData();
    formData.append("file", file);
    const response = await fetch("/upload", {
        method: "POST",
        body: formData
    });

    const data = await response.json();
    console.log(data);
    console.log(Object.keys(data));
    totalRevenue.textContent = data.analytics.total_revenue;
    totalTransactions.textContent = data.analytics.total_transactions;
    totalQuantity.textContent = data.analytics.total_quantity;
    averageTransaction.textContent = data.analytics.average_transaction_value;
    grossRevenue.textContent=data.analytics.gross_revenue;
    const charts = [
    revenueCategoryChart,
    transactionsCategoryChart,
    topCategoriesChart,
    quantityCategoryChart,
    revenueRegionChart,
    revenueYearChart,
    revenueMonthChart
];
    console.log("ABOUT TO DESTROY OLD CHARTS");
    charts.forEach(function(canvas) {
    const chart = Chart.getChart(canvas);
    console.log("Existing chart:", chart);
    if (chart) {
        chart.destroy();
    }
});
    createRevenueCategoryChart(data);
    createTransactionsCategoryChart(data);
    createTopCategoriesChart(data);
    createQuantityCategoryChart(data); 
    createRevenueRegionChart(data);
    createRevenueYearChart(data);
    createRevenueMonthChart(data);
    
});
