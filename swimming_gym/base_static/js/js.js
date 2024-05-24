function renderiza_grafico(url, canva_id, color){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        const ctx = document.getElementById(canva_id).getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.labels,
                datasets: [{
                    data: data.data,
                    backgroundColor: color,
                    borderColor: 'rgba(128,128,128,1)',
                    borderWidth: 1,
                    fill: true
                }]
            },
            options: {
                responsive: true,
                legend: {
                        display: false // Define a legenda como não exibida
                    },
                plugins: {
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return context.yLabel; // Retorna apenas o valor do ponto de dados
                            }
                        }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            },
        });
    })
}
