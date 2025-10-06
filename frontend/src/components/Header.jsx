import { BoltIcon } from '@heroicons/react/24/solid'

/**
 * Cabeçalho fixo da aplicação com uma mensagem de boas-vindas.
 */
function Header() {
  return (
    <header className="border-b border-slate-200 bg-white/80 backdrop-blur">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
        <div className="flex items-center gap-3">
          <span className="flex h-10 w-10 items-center justify-center rounded-full bg-blue-600 text-white">
            <BoltIcon className="h-6 w-6" />
          </span>
          <div>
            <h1 className="text-lg font-semibold text-slate-900">Cartório Inteligente</h1>
            <p className="text-sm text-slate-500">
              Organize, processe e exporte dados de documentos cartoriais em poucos cliques.
            </p>
          </div>
        </div>
      </div>
    </header>
  )
}

export default Header
