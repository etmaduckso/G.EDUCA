package com.service.data

import androidx.recyclerview.widget.LinearLayoutManager

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.service.data.databinding.ActivityProdutosBinding

class ProdutosActivity : AppCompatActivity() {
    private lateinit var binding: ActivityProdutosBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityProdutosBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Configurar ActionBar
        supportActionBar?.apply {
            title = "Produtos"
        }

        // Inicializar o RecyclerView
        val recyclerView = binding.recyclerViewProdutos
        recyclerView.layoutManager = LinearLayoutManager(this)

        // Criar uma lista de produtos de exemplo
        val produtos = listOf(
            Produto("Produto 1", "Descrição do Produto 1", 50.0),
            Produto("Produto 2", "Descrição do Produto 2", 75.0),
            Produto("Produto 3", "Descrição do Produto 3", 100.0)
        )

        // Configurar o Adapter
        val adapter = ProdutoAdapter(produtos)
        recyclerView.adapter = adapter
    }
}
