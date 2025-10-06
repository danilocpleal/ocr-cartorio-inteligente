/**
 * Exibe a tabela com os dados extraídos pelo backend.
 */
function ResultsTable({ documentos }) {
  if (!documentos || documentos.length === 0) {
    return (
      <div className="rounded-3xl border border-dashed border-slate-300 p-10 text-center text-slate-400">
        Os resultados aparecerão aqui após o processamento.
      </div>
    )
  }

  const linhas = documentos.flatMap((doc) => {
    const max = Math.max(
      doc.nomes.length,
      doc.cpfs.length,
      doc.qualidade_nomes.length,
      doc.qualidade_cpfs.length,
      doc.situacoes.length,
      1
    )

    return Array.from({ length: max }).map((_, index) => ({
      arquivo: doc.arquivo,
      nome: doc.nomes[index] ?? '',
      qualidadeNome: doc.qualidade_nomes[index] ?? '',
      cpf: doc.cpfs[index] ?? '',
      qualidadeCpf: doc.qualidade_cpfs[index] ?? '',
      situacao: doc.situacoes[index] ?? '',
      aberturas: doc.aberturas.join(', '),
      registros: doc.registros.join(', '),
      averbacoes: doc.averbacoes.join(', '),
    }))
  })

  return (
    <div className="overflow-hidden rounded-3xl border border-slate-200 bg-white shadow-xl">
      <div className="max-h-96 overflow-y-auto">
        <table className="min-w-full divide-y divide-slate-200">
          <thead className="bg-slate-900 text-white">
            <tr>
              <th scope="col" className="px-4 py-3 text-left text-xs font-semibold uppercase tracking-wide">
                Arquivo
              </th>
              <th scope="col" className="px-4 py-3 text-left text-xs font-semibold uppercase tracking-wide">
                Nome
              </th>
              <th scope="col" className="px-4 py-3 text-left text-xs font-semibold uppercase tracking-wide">
                Qualidade Nome
              </th>
              <th scope="col" className="px-4 py-3 text-left text-xs font-semibold uppercase tracking-wide">
                CPF
              </th>
              <th scope="col" className="px-4 py-3 text-left text-xs font-semibold uppercase tracking-wide">
                Qualidade CPF
              </th>
              <th scope="col" className="px-4 py-3 text-left text-xs font-semibold uppercase tracking-wide">
                Situação
              </th>
              <th scope="col" className="px-4 py-3 text-left text-xs font-semibold uppercase tracking-wide">
                Aberturas
              </th>
              <th scope="col" className="px-4 py-3 text-left text-xs font-semibold uppercase tracking-wide">
                Registros
              </th>
              <th scope="col" className="px-4 py-3 text-left text-xs font-semibold uppercase tracking-wide">
                Averbações
              </th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100 bg-white">
            {linhas.map((linha, index) => (
              <tr key={`${linha.arquivo}-${index}`} className="hover:bg-blue-50/60">
                <td className="whitespace-nowrap px-4 py-2 text-sm text-slate-600">{linha.arquivo}</td>
                <td className="whitespace-nowrap px-4 py-2 text-sm text-slate-700">{linha.nome}</td>
                <td className="whitespace-nowrap px-4 py-2 text-sm text-slate-500">{linha.qualidadeNome}</td>
                <td className="whitespace-nowrap px-4 py-2 text-sm text-slate-700">{linha.cpf}</td>
                <td className="whitespace-nowrap px-4 py-2 text-sm text-slate-500">{linha.qualidadeCpf}</td>
                <td className="whitespace-nowrap px-4 py-2 text-sm text-slate-500">{linha.situacao}</td>
                <td className="whitespace-nowrap px-4 py-2 text-sm text-slate-500">{linha.aberturas}</td>
                <td className="whitespace-nowrap px-4 py-2 text-sm text-slate-500">{linha.registros}</td>
                <td className="whitespace-nowrap px-4 py-2 text-sm text-slate-500">{linha.averbacoes}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}

export default ResultsTable
