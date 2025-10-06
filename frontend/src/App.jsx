import { useState } from 'react'
import { FolderIcon, Cog6ToothIcon } from '@heroicons/react/20/solid'

function App() {
  const [files, setFiles] = useState([])

  const handleDirectoryUpload = (event) => {
    const selectedFiles = Array.from(event.target.files)
    setFiles(selectedFiles)
  }

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col md:flex-row">
      {/* Sidebar */}
      <aside className="w-full md:w-56 bg-white shadow-md p-4 flex flex-col">
        <h1 className="text-lg font-bold text-gray-800 mb-6">Cartório Inteligente</h1>
        <nav className="space-y-4">
          <div className="flex items-center gap-2 text-gray-700 text-sm font-medium hover:text-blue-600 cursor-pointer">
            <FolderIcon className="w-4 h-4" />
            <span>Upload</span>
          </div>
          <div className="flex items-center gap-2 text-gray-500 text-sm hover:text-blue-600 cursor-pointer">
            <Cog6ToothIcon className="w-4 h-4" />
            <span>Configurações</span>
          </div>
        </nav>
      </aside>

      {/* Main content */}
      <main className="flex-1 px-6 py-10 flex flex-col items-center justify-center text-gray-800">
        <h2 className="text-xl font-bold mb-1 text-center">OCR de Documentos</h2>
        <p className="text-xs text-gray-500 mb-6 text-center">via seleção de diretório</p>

        <div className="w-full max-w-md bg-white rounded-lg shadow p-5 mb-6">
          <label className="block mb-2 text-sm font-medium">
            Selecione uma pasta com documentos:
          </label>
          <input
            type="file"
            webkitdirectory="true"
            directory="true"
            onChange={handleDirectoryUpload}
            className="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 p-2 focus:outline-none"
          />
          <p className="mt-2 text-xs text-gray-500">
            {files.length === 0 ? 'Nenhum arquivo escolhido' : `${files.length} arquivos selecionados`}
          </p>
        </div>

        <button
          className="w-full max-w-md py-2.5 bg-blue-600 text-white text-sm font-semibold rounded hover:bg-blue-700 disabled:opacity-50"
          disabled={files.length === 0}
          onClick={() => alert('Enviar para backend (em breve)')}
        >
          Processar documentos
        </button>

        <div className="mt-10">
          <img
            src="https://cdn-icons-png.flaticon.com/512/3062/3062634.png"
            alt="Ilustração OCR"
            className="w-32 h-32 mx-auto"
          />
        </div>
      </main>
    </div>
  )
}

/*import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Resultados from './pages/Resultados'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Resultados />} />
        {/* Outras rotas futuras }
      </Routes>
    </Router>
  )
}*/

export default App