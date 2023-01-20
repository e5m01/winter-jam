




"Non sai di preciso come sei arrivato fino a qui. C'è un vuoto nella tua testa."
"Ma riesci ancora a ricordarti chi sei, e cosa ci fai qui."
"Sei un game developer di uno studio di videogiochi molto importante, e hai usato i tuoi risparmi per fare un viaggio con i tuoi amici per l'Inghilterra, dove vivete."
"Siete tutti appassionati delle storie horror e dei giochi da tavolo, e nel gruppo ci sono un paio di Narrative Designer..."
"... che, quando hanno visto il nome di Innsmouth nella mappa, si sono incuriositi."
"Vi hanno fatto sapere che Innsmouth è il nome di fantasia di una cittadina americana, in una delle storie di Lovecraft."
"Eravate comunque di passaggio e stava tramontando il sole. Così avete deciso che passare una notte a Innsmouth sarebbe stato elettrizzante."
"Ma il resto, non appena avete attraversato il confine di quella inquietante cittadina... è confuso, nelle tue memorie."
"Osservi l'inquietante maniero che si staglia davanti a te. Guglie sottili che si protendono oblique verso il cielo, con mattonelle annerite come se fossero sopravvissute a un incendio."
"Persino la pietra grigia di cui è costituito l'esterno del castello, quella ricorda un pallore insano, prossimo alla morte."
"Tutto attorno al maniero, gli alberi malati e senza foglie sembrano piegarsi nella sua direzione, con articolazioni irregolari e sinistre dei rami, in una espressione di dolore."
"Ti guardi attorno, e ti accorgi... che sei inghiottito dal buio. Non vedi niente alle tue spalle- ma senti i cigolii del legno, il fruscio confuso delle foglie, e suoni che non riesci bene a comprendere."
"Un brivido percorre il tuo corpo. Dove sono gli altri? Che fine hanno fatto? Non c'è traccia di loro, e tu inizi a pensare che dovresti trovare un riparo dall'oscurità."
"Così ti incammini all'ingresso del maniero."

#Room shift to "Entrance Hall", but no label jump.

"Nonostante le luci accese, la tua prima impressione è che questo luogo sia stato abbandonato a sé stesso."
"L'aria di questo luogo sembra più rarefatta- come una nebbia altamente improbabile. Potrebbe essere polvere, o cenere."
"Ti trovi in quello che sembrerebbe essere una grande entrance hall, con delle scale che portano verso l'alto."
"Una delle stanze al piano di sopra sembra aperta, forse uno studio di qualche genere."
"L'altra parte della scala, invece, porta direttamente all'attico."
"Questo piano sembra portare a un lungo corridoio, difficile sapere dove potrebbe farti finire."


#Choice: "Library" "Attic" "Corridor"

#if Library: jump to "Library"
"Ti trovi in un polveroso studio. L'odore della carta vecchia e dell'inchiostro riempiono le tue narici."
"Davanti a te si trova una scrivania di legno pregiato, dalle gambe ondulate e la superficie ricoperta da una lastra di vetro in cui sono intagliate decorazioni eleganti."
"Impossibile decifrare le decorazioni, perché il tavolo è quasi del tutto impegnato da tomi disordinatamente impilati l'uno sull'altro, documenti ingialliti, penne stilografiche e pennini ad inchiostro."
"Le pareti della stanza sono quasi del tutto occupate da librerie alte fino al soffitto, con una quantità innumerevole di libri e di soprammobili."
"Ti guardi attorno, e la tua attenzione viene catturata da un artefatto che, tra tutti, sembra strano trovare proprio in uno studio."
"Si tratta di una spada dalle sembianze piuttosto antiche, forgiata in un metallo che ti sembra alieno e che, per il colore, potresti forse ricondurre al rame."
"La spada dev'essere di un tipo cerimoniale, perché è tempestata di decorazioni sull'elsa, sulla guardia e sulla base della lama stessa."
"In particolare, proprio lì giace la figura di una creatura immonda che non hai mai visto prima. La sua testa è incoronata da un rubino."
"Vuoi prendere la spada?"

#Choice: Yes / No
#If yes, maybe, add sound of item taken
#in both cases, the story goes on like this:

"Torni verso la porta, e nel farlo senti un tonfo. Hai fatto cadere un libro per sbaglio."
"Quando lo prendi per rimetterlo a posto, noti che si tratta di un tomo grigio come il fumo, dalla copertina in pelle, dove sono inscritti dei simboli."
"Sembrano dei simboli occulti che vanno attorno a un cerchio, e in basso un titolo:"
"T'tka Halot."
"Lo apri. Il libro contiene una serie di illustrazioni fatte a mano, così antiche che l'inchiostro, prima nero, ha cambiato colore insieme all'ingiallimento delle pagine."
"Non comprendi niente di ciò che vi è scritto, ma sembrano una sorta di canti."
"Vuoi prendere il T'tka Halot?"

#Choice: Yes / No
#If yes, maybe, add sound of item taken
#in both cases, the story goes on like this:

#Choice: "Attic" or "Corridor"


#if Attic: jump to "Attic"


"Salendo le scale che portano verso l'attico, ti rendi conto che la luce non raggiunge il piano superiore."
"Cerchi di aiutarti con la torcia del cellulare."

#if possible, EFFECT of flash

#SOUND of stairs creaking (maybe same sound as the woodboard)
"Le scale scricchiolano sotto i tuoi piedi, illuminate dalla luce tagliente e intensa della torcia."
"Esse ti portano a un breve pianerottolo, e davanti a te si trova una porta."
#SOUND of door handle creaking while opening
"Cerchi di aprirla. La maniglia di ottone cigola, mentre ti asseconda."
"Davanti a te si trova una stanza polverosa, ricolma di cianfrusaglie che, sotto la luce fredda, sembrano assumere forme distorte e allungate, fondendosi con la loro stessa ombra..."
"... al punto che non sei più sicuro di dove finisce la sagoma di un tappeto persiano arrotolato..."
"... e dove inizia l'angolo di una vecchia tenda, posta vicino alla finestra."
"Non c'è traccia dei tuoi amici qui. Né di qualcosa di utile. Ma forse puoi trovare delle informazioni su cosa sia questo maniero..."
"Ti guardi attorno. Vecchie fotografie, libri ammuffiti, specchi coperti da drappi ingialliti."
"Una scatola di stoffa, tra le altre cose, sembra contenere una serie di documenti."
"Vuoi dare un'occhiata?"

#Choice: Yes / No
#If no, jump to label noclue
#If yes, maybe, add SOUND of clue and:

"Ti accovacci per cercare qualcosa di interessante tra le cartelle, le mappe edili e i fogli ingialliti."
"La tua mano pesca una vecchia foto. Raffigura un uomo, una donna e due bambini, in posa dietro il maniero."
"Il maniero sembra molto simile a quello in cui ti trovi adesso. L'uomo e la donna sorridono, sembrano felici."
"C'è qualcosa nei loro sguardi che non ti convince, però. Il loro è uno sguardo vitreo, e al collo indossano dei pendenti."
"Avvicini la torcia alla foto per cercare di vedere meglio. Quei pendenti sembrano avere la forma di un animale marino, come una piovra, o un polipo."
"Indossano abiti eleganti, di quelli in voga non più di 70 anni fa."
"Porti di nuovo lo sguardo sulla scatola di tessuto, e una delle mappe del maniero attira la tua attenzione. Allunghi la mano, e la porti davanti alla luce della torcia."
#SOUND of paper
"La mappa sembra raffigurare accuratamente i piani del maniero. L'attico, dove ti trovi tu, è il piano più in alto."
"Sotto si trovano lo studio, un bagno, e un paio di altre stanze di cui non riesci bene a comprendere la funzione."
"Dopodiché il corridoio sembra portare alle cucine, e alle camere da letto."
"Corrughi la fronte quando noti che i piani, in realtà, non sono finiti."
"Sembra esserci un seminterrato. Ma la cosa più strana è che la porta d'accesso del seminterrato sembra trovarsi..."
"... in una delle camere da letto, attraverso una botola."
"Non sai perché, ma inizi a sentire i peli delle braccia sollevarsi, e un brivido partire dalla tua nuca, come se il tuo istinto di sopravvivenza avesse notato qualcosa che tu non hai notato."
"Sospiri, e stai per rimettere tutto a posto, quando vedi un simbolo vicino al disegno della botola."
"E' lo stesso simbolo che hai visto al collo dei due proprietari di casa."
"Quel dettaglio ti rimane in testa mentre abbandoni i documenti nella scatola, alzandoti."

#jump to label noclue

#label noclue:

#Choice: "Library" or "Corridor"

#if Corridor: jump to "Corridor" (or "Bedroom")

"Ti incammini verso il corridoio del piano terra. Prosegui lungo il corridoio, e ti sembra di sentire, da dentro il maniero, ancora il cigolio dei rami all'esterno."
"Forse è il suono delle assi del pavimento sotto il tuo peso. O dei mobili di legno, per l'umidità. Forse c'è qualcuno...? I tuoi amici..?"
"Ti gira un po' la testa, e man mano che prosegui, accendendo la torcia del tuo cellulare per vedere con chiarezza, inizi a percepire un forte mal di testa che ti afferra."
"Ti fermi quando ti accorgi di una luce provenire da una delle camere. La porta è aperta."
"Accedi, osservi la stanza. Il letto è in diagonale, come se fosse stato spostato. A terra, nella posizione dove esso si trovava, sembra esserci una botola."
"La botola era fissa al pavimento da una catena serrata attorno a due cerchi di metallo fusi con le assi di legno. Quella catena, ora, è sbrogliata."
"Qualcosa dentro di te è attratto dalla curiosità di vedere cosa c'è sotto. L'altra parte di te, invece, ha l'impressione che gli angoli delle pareti si stiano rattrappendo contro se stesse, che la stanza stia venendo risucchiata da quella stessa botola."
"Il mal di testa è ancora più forte."
"E' tua la scelta, ma qualcosa ti dice che se scenderai nella botola, non potrai più tornare indietro."

#Choice: "Go down" or "Don't go down"
#If "Don't go down":
#Choice: "Attic" or "Library"
#If "Go down", jump to "Ocean Cave"


#label "Ocean Cave":
