function DocumentoCard({ doc }) {
  return (
    <div className="bg-white rounded-lg shadow p-4 mb-4 w-full max-w-xl">
      <h3 className="text-lg font-semibold text-gray-800">{doc.nome_arquivo}</h3>
      <p className="text-sm text-gray-500 mb-2">Tipo: {doc.tipo} | Extraído em: {doc.data_extracao}</p>
      <div className="bg-gray-50 p-3 rounded text-sm text-gray-700 whitespace-pre-line">
        {doc.texto.slice(0, 200)}...
      </div>
      <div className="mt-3 flex justify-between items-center">
        <span className={`text-xs font-medium px-2 py-1 rounded ${
          doc.status === 'Processado' ? 'bg-green-100 text-green-700' : 'bg-yellow-100 text-yellow-700'
        }`}>
          {doc.status}
        </span>
        <button className="text-blue-600 text-sm hover:underline">Ver completo</button>
      </div>
    </div>
  )
}

export default DocumentoCard