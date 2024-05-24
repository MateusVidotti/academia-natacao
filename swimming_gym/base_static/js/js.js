function gera_cor(qtd=1){
    var bg_color = []
    var border_color = []
    for(let i = 0; i < qtd; i++){
        let r = Math.random() * 255;
        let g = Math.random() * 255;
        let b = Math.random() * 255;
        bg_color.push(`rgba(${r}, ${g}, ${b}, ${0.2})`)
        border_color.push(`rgba(${r}, ${g}, ${b}, ${1})`)
    }
    return [bg_color, border_color];
}


function renderiza_grafico(url, canva_id, type){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        const ctx = document.getElementById(canva_id).getContext('2d');
        var cores_faturamento_mensal = gera_cor(qtd=12)
        const myChart = new Chart(ctx, {
            type: type,
            data: {
                labels: data.labels,
                datasets: [{
                    data: data.data,
                    backgroundColor: cores_faturamento_mensal[0],
                    borderColor: cores_faturamento_mensal[1],
                    borderWidth: 1
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
            }
        });
    })
}
