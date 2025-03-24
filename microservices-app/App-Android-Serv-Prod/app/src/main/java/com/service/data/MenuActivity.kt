package com.service.data

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.service.data.databinding.ActivityMenuBinding

class MenuActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMenuBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMenuBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Configurar ActionBar
        supportActionBar?.apply {
            title = "Menu"
        }

        // Configurar cliques para navegar para as atividades de serviços e produtos
        binding.buttonServicos.setOnClickListener {
            startActivity(Intent(this, ServicosActivity::class.java))
        }

        binding.buttonProdutos.setOnClickListener {
            startActivity(Intent(this, ProdutosActivity::class.java))
        }
    }
}
