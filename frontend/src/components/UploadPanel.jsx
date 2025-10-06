import { CloudArrowUpIcon } from '@heroicons/react/24/outline'

/**
 * Painel responsável por receber os arquivos do usuário.
 */
function UploadPanel({ onFilesSelected, isProcessing, onProcessClick, files, processingEnabled }) {
  return (
    <section className="rounded-3xl border border-slate-200 bg-white p-8 shadow-xl">
      <header className="flex items-start justify-between">
        <div>
          <h2 className="text-lg font-semibold text-slate-900">Selecione os documentos</h2>
          <p className="mt-1 text-sm text-slate-500">
            Arraste arquivos em PDF ou imagem, ou clique para escolher manualmente.
          </p>
        </div>
      </header>

      <label
        className="mt-6 flex cursor-pointer flex-col items-center justify-center gap-3 rounded-2xl border-2 border-dashed border-slate-300 bg-slate-50 p-10 text-center transition hover:border-blue-400 hover:bg-blue-50"
      >
        <CloudArrowUpIcon className="h-12 w-12 text-blue-500" />
        <div>
          <p className="text-sm font-medium text-slate-700">
            Solte os arquivos aqui ou <span className="text-blue-600">clique para enviar</span>
          </p>
          <p className="mt-1 text-xs text-slate-400">Suporta PDF, JPG, PNG e TIFF</p>
        </div>
        <input
          type="file"
          className="hidden"
          multiple
          accept=".pdf,.jpg,.jpeg,.png,.tiff"
          onChange={(event) => onFilesSelected(Array.from(event.target.files))}
        />
      </label>

      <div className="mt-6 rounded-2xl border border-slate-100 bg-slate-50 p-4">
        <p className="text-sm font-semibold text-slate-700">
          {files.length === 0 ? 'Nenhum arquivo selecionado' : `${files.length} arquivo(s) pronto(s) para envio.`}
        </p>
        {files.length > 0 ? (
          <ul className="mt-3 grid max-h-40 gap-2 overflow-y-auto text-xs text-slate-500">
            {files.map((file) => (
              <li key={file.name} className="flex items-center justify-between gap-3 rounded-lg bg-white px-3 py-2 shadow-sm">
                <span className="truncate" title={file.name}>
                  {file.name}
                </span>
                <span className="whitespace-nowrap text-[11px] text-slate-400">
                  {(file.size / 1024).toFixed(1)} KB
                </span>
              </li>
            ))}
          </ul>
        ) : null}
      </div>

      <button
        type="button"
        onClick={onProcessClick}
        disabled={!processingEnabled || isProcessing}
        className="mt-6 w-full rounded-2xl bg-blue-600 py-3 text-sm font-semibold text-white shadow-lg transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:bg-slate-300"
      >
        {isProcessing ? 'Processando...' : 'Processar documentos'}
      </button>
    </section>
  )
}

export default UploadPanel
