import DocumentoCard from '../components/Documentocard'

const documentos = [
  {
    nome_arquivo: "CertidaoNascimento.pdf",
    tipo: "PDF",
    data_extracao: "2025-10-05",
    texto: "CERTIDÃO DE NASCIMENTO\nDanilo Oliveira, nascido em 12/03/1990...",
    status: "Processado"
  },
  {
    nome_arquivo: "ReconhecimentoFirma.jpg",
    tipo: "Imagem",
    data_extracao: "2025-10-05",
    texto: "RECONHECIMENTO DE FIRMA\nAssinatura de João Silva...",
    status: "Processado"
  }
]

function Resultados() {
  return (
    <div className="min-h-screen bg-gray-100 px-4 py-8 flex flex-col items-center">
      <h2 className="text-2xl font-bold text-gray-800 mb-6">Resultados do OCR</h2>
      {documentos.map((doc, index) => (
        <DocumentoCard key={index} doc={doc} />
      ))}
    </div>
  )
}

export default Resultados