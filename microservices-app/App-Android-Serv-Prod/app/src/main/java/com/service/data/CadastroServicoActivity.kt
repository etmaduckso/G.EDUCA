package com.service.data

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.ImageView
import android.widget.Spinner
import androidx.appcompat.app.AppCompatActivity

class CadastroServicoActivity : AppCompatActivity() {

    private lateinit var tipoServicoSpinner: Spinner
    private lateinit var nomeServicoEditText: EditText
    private lateinit var descricaoServicoEditText: EditText
    private lateinit var imagemServicoImageView: ImageView
    private lateinit var salvarButton: Button
    private lateinit var editarButton: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.cadastro_servico)

        tipoServicoSpinner = findViewById(R.id.tipoServicoSpinner)
        nomeServicoEditText = findViewById(R.id.nomeServicoEditText)
        descricaoServicoEditText = findViewById(R.id.descricaoServicoEditText)
        imagemServicoImageView = findViewById(R.id.imagemServicoImageView)
        salvarButton = findViewById(R.id.salvarButton)
        editarButton = findViewById(R.id.editarButton)

        salvarButton.setOnClickListener {
            // Lógica para salvar o serviço
        }

        editarButton.setOnClickListener {
            // Lógica para editar o serviço
        }
    }
}
