(definitions)=
# Definitions


:::{warning}
Currently, definitions and theorems are just listed here. They will be sorted later.
:::

:::{prf:definition} Realization
:label: def-realization

Let $G=(V_G,E_G)$ be a simple graph, $\KK$ be a field and $d\in\NN$.
A $d$-dimensional _realization_ of $G$ in $\KK^d$ is a map $p\colon V_G\rightarrow \KK^d$.

The realization $p$ is _quasi-injective_ if $p(u)\neq p(v)$ for every edge $uv\in E_G$.
:::

:::{prf:definition} Framework
:label: def-framework

Let $G$ be a graph and let $p$ be a $d$-dimensional {prf:ref}`realization <def-realization>` of $G$.
The pair $(G, p)$ is a called a _framework_.

{{pyrigi_crossref}} {class}`~pyrigi.framework.Framework`
{meth}`~.Framework.underlying_graph`
{meth}`~.Framework.get_realization`
:::

:::{prf:definition} (Generically) rigid graph
:label: def-gen-rigid

Let $G$ be a graph and $d \in \NN$.
The graph $G$ is (generically) $d$-rigid if ...

{{pyrigi_crossref}} {meth}`~.Graph.is_rigid`
:::

:::{prf:definition} $(k, \ell)$-sparse and $(k, \ell)$-tight
:label: def-kl-sparse-tight

Let $G = (V_G, E_G)$ be a (multi)graph and let $k, \ell \in \NN$.
Set $n = |V_G|$ and $m = |E_G|$.
The graph $G$ is said to be _$(k, \ell)$-sparse_ if every set of $n' \leq n$ vertices spans at most $kn' - \ell$ edges.
The graph $G$ is said to be _$(k, \ell)$-sparse_ if it is $(k, \ell)$-sparse and $kn - \ell = m$.

{{pyrigi_crossref}} {meth}`~.Graph.is_sparse`
{meth}`~.Graph.is_tight`

{{references}} {cite:p}`Lee2008`
:::



:::{prf:definition} Infinitesimally rigid frameworks
:label: def-inf-rigid-framework

A framework is called _infinitesimally rigid_, if all its infinitesimal flexes are trivial. 
This is the case when either there is less than 1 vertex in the framework, making it 
trivially rigid, or the rigidity matrix has rank $d \cdot |V| - {d\choose 2}$, since 
there are ${d\choose 2}$ isometries of $\RR^d$.
{{pyrigi_crossref}} {meth}`~.Framework.is_inf_rigid`
:::

:::{prf:definition} Minimally and redundantly rigid frameworks
:label: def-minimally-redundantly-rigid-framework

Let $G$ be a graph, let $d, k \in \NN$, and let $p$ be a $d$-dimensional {prf:ref}`realization <def-realization>` of $G$.
The framework $(G, p)$ is called _minimally $d$-rigid_ if ...
The framework $(G, p)$ is called _redundantly $d$-rigid_ if ...
The framework $(G, p)$ is called _vertex redundantly $d$-rigid_ if ...
The framework $(G, p)$ is called _$k$-redundantly $d$-rigid_ if ...
The framework $(G, p)$ is called _$k$-vertex redundantly $d$-rigid_ if ...

{{pyrigi_crossref}} {meth}`~.Framework.is_redundantly_rigid`
:::


:::{prf:definition} Minimally and redundantly generically rigid graphs
:label: def-minimally-redundantly-rigid-graph

Let $G$ be a graph, let $d, k \in \NN$.
The graph $G$ is called _minimally (generically) $d$-rigid_ if ...
The graph $G$ is called _redundantly (generically) $d$-rigid_ if ...
The graph $G$ is called _vertex redundantly (generically) $d$-rigid_ if ...
The graph $G$ is called _$k$-redundantly (generically) $d$-rigid_ if ...
The graph $G$ is called _$k$-vertex redundantly (generically) $d$-rigid_ if ...

{{pyrigi_crossref}} {meth}`~.Graph.is_minimally_rigid`
{meth}`~.Graph.is_redundantly_rigid`
{meth}`~.Graph.is_vertex_redundantly_rigid`
{meth}`~.Graph.is_k_redundantly_rigid`
{meth}`~.Graph.is_k_vertex_redundantly_rigid`
:::

:::{prf:theorem}
:label: thm-2-gen-rigidity

A graph $G = (V_G, E_G)$ is generically $2$-rigid if and only if ...

{{references}} {cite:p}`Geiringer1927`
{cite:p}`Laman1970`
:::
