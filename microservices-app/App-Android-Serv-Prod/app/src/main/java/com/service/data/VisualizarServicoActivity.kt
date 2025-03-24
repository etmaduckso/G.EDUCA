package com.service.data

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.service.data.databinding.ActivityVisualizarServicoBinding

class VisualizarServicoActivity : AppCompatActivity() {
    private lateinit var binding: ActivityVisualizarServicoBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityVisualizarServicoBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Configurar ActionBar
        supportActionBar?.apply {
            title = "Visualizar Serviço"
        }

        // Aqui você pode configurar a exibição dos detalhes do serviço
    }
}
