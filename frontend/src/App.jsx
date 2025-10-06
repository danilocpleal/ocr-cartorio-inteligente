import { useMemo, useState } from 'react'
import { ArrowPathIcon, DocumentCheckIcon, FolderIcon } from '@heroicons/react/24/outline'

import Header from './components/Header'
import ResultsTable from './components/ResultsTable'
import StatusBanner from './components/StatusBanner'
import SummaryCard from './components/SummaryCard'
import UploadPanel from './components/UploadPanel'
import { processarDocumentos } from './utils/api'

function App() {
  const [files, setFiles] = useState([])
  const [isProcessing, setIsProcessing] = useState(false)
  const [error, setError] = useState('')
  const [resultado, setResultado] = useState(null)

  const totalRegistros = useMemo(() => {
    if (!resultado?.dados_extraidos) return 0
    return resultado.dados_extraidos.reduce(
      (acc, doc) => acc + Math.max(doc.nomes.length, doc.cpfs.length, 1),
      0
    )
  }, [resultado])

  const handleFilesSelected = (selectedFiles) => {
    setFiles(selectedFiles)
    setError('')
  }

  const handleProcess = async () => {
    if (files.length === 0) return

    try {
      setIsProcessing(true)
      setError('')
      const response = await processarDocumentos(files)
      setResultado(response)
    } catch (processingError) {
      setError(processingError.message)
    } finally {
      setIsProcessing(false)
    }
  }

  const resumo = resultado?.resumo

  return (
    <div className="min-h-screen bg-slate-100">
      <Header />

      <main className="mx-auto grid max-w-6xl gap-8 px-6 py-10 lg:grid-cols-[1.1fr_0.9fr]">
        <section className="lg:col-span-1">
          <UploadPanel
            files={files}
            onFilesSelected={handleFilesSelected}
            onProcessClick={handleProcess}
            isProcessing={isProcessing}
            processingEnabled={files.length > 0}
          />

          <div className="mt-6 space-y-3">
            <StatusBanner
              type={error ? 'error' : 'info'}
              message={
                error ||
                'Os arquivos enviados são armazenados temporariamente e podem ser exportados em Excel, HTML ou JSON.'
              }
            />
            {resumo ? (
              <StatusBanner
                type="success"
                message={`Exportação gerada em: ${resumo.arquivo_exportado}`}
              />
            ) : null}
          </div>
        </section>

        <section className="space-y-6">
          <div className="grid gap-4 md:grid-cols-3">
            <SummaryCard
              title="Arquivos processados"
              value={resumo?.quantidade_arquivos ?? 0}
              description="Quantidade total de documentos recebidos nesta execução."
              icon={FolderIcon}
              tone="blue"
            />
            <SummaryCard
              title="Registros mapeados"
              value={totalRegistros}
              description="Somatório de nomes/CPFs identificados."
              icon={DocumentCheckIcon}
              tone="emerald"
            />
            <SummaryCard
              title="Motor selecionado"
              value={resumo?.motor_usado ?? 'Aguardando envio'}
              description={resumo ? `Arquivo exportado: ${resumo.arquivo_exportado}` : 'O motor é escolhido automaticamente.'}
              icon={ArrowPathIcon}
              tone="slate"
            />
          </div>

          <ResultsTable documentos={resultado?.dados_extraidos ?? []} />
        </section>
      </main>
    </div>
  )
}

export default App
