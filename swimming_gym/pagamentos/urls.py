from django.urls import path
from pagamentos import views

app_name = 'pagamentos'

urlpatterns = [
    path('', views.pagamentos_views, name='pagamentos'),
    path('adicionar/', views.adicionar_pagamento, name='adicionar_pagamento'),
    path('editar/<pagamento_id>', views.editar_pagamento, name='editar_pagamento'),
    path('deletar/<pagamento_id>', views.delete_pagamento, name='delete_pagamento'),
    path('relatorio_pagamento', views.relatorio_pagamento, name="relatorio_pagamento"),
]
