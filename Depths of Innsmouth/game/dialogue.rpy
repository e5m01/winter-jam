




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
#If yes, maybe, add sound of clue and:


#If no:
#Choice: "Library" or "Corridor"
