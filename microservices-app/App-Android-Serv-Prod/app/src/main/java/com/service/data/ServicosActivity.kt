package com.service.data

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.service.data.databinding.ActivityServicosBinding

class ServicosActivity : AppCompatActivity() {
    private lateinit var binding: ActivityServicosBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityServicosBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Configurar ActionBar
        supportActionBar?.apply {
            title = "Serviços"
        }

        // Inicializar o RecyclerView
        val recyclerView = binding.recyclerViewServicos
        recyclerView.layoutManager = LinearLayoutManager(this)

        // Criar uma lista de serviços de exemplo
        val servicos = listOf(
            Servico("Serviço 1", "Descrição do Serviço 1", 100.0),
            Servico("Serviço 2", "Descrição do Serviço 2", 150.0),
            Servico("Serviço 3", "Descrição do Serviço 3", 200.0)
        )

        // Configurar o Adapter
        val adapter = ServicoAdapter(servicos)
        recyclerView.adapter = adapter

        // Adicionar botão de cadastrar serviço
        binding.cadastrarServicoButton.setOnClickListener {
            val intent = Intent(this, CadastroServicoActivity::class.java)
            startActivity(intent)
        }
    }
}