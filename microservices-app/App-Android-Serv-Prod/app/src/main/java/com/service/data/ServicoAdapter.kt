package com.service.data

import android.content.Intent
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class ServicoAdapter(private val servicos: List<Servico>) : RecyclerView.Adapter<ServicoAdapter.ServicoViewHolder>() {

    class ServicoViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val nome: TextView = itemView.findViewById(android.R.id.text1)
        val descricao: TextView = itemView.findViewById(android.R.id.text2)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ServicoViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(android.R.layout.simple_list_item_2, parent, false)
        return ServicoViewHolder(view)
    }

    override fun onBindViewHolder(holder: ServicoViewHolder, position: Int) {
        val servico = servicos[position]
        holder.nome.text = servico.nome
        holder.descricao.text = servico.descricao

        // Adicionar listener de clique
        holder.itemView.setOnClickListener {
            val context = holder.itemView.context
            val intent = Intent(context, VisualizarServicoActivity::class.java)
            // Passar dados do serviço, se necessário
            context.startActivity(intent)
        }
    }

    override fun getItemCount(): Int {
        return servicos.size
    }
}
