import gmpy2 
def legendre_symbol(n,p):
    return pow(n,(p-1)//2,p)

def tonelli_shanks(n,p):
    if n%p==0:
        return 0
    if p%4==3:
        return pow(n,(p+1)//4,p)
    q = p-1
    s = 0
    while q%2==0:
        s+=1
        q=q//2
    # print(f"q = {q}")
    # print(f"s = {s}")
    z = 2
    while legendre_symbol(z,p)==1:
        z+=1
    # print(f"z = {z}")
    m = s
    c = pow(z,q,p)
    t = pow(n,q,p)
    r = pow(n,(q+1)//2,p)
    # print(f"m = {m}") 
    # print(f"c = {c}")
    # print(f"t = {t}")
    # print(f"r = {r}")
    while t!=1:
        i = 0
        temp = t
        while temp!=1:
            i+=1
            temp = (temp*temp)%p
        expo = 2**(m-i-1)
        b = pow(c,expo,p)
        m = i
        c = (b * b)%p
        t = (t * b * b)%p
        r = (r * b)%p
    return r

a = 8479994658316772151941616510097127087554541274812435112009425778595495359700244470400642403747058566807127814165396640215844192327900454116257979487432016769329970767046735091249898678088061634796559556704959846424131820416048436501387617211770124292793308079214153179977624440438616958575058361193975686620046439877308339989295604537867493683872778843921771307305602776398786978353866231661453376056771972069776398999013769588936194859344941268223184197231368887060609212875507518936172060702209557124430477137421847130682601666968691651447236917018634902407704797328509461854842432015009878011354022108661461024768
p = 30531851861994333252675935111487950694414332763909083514133769861350960895076504687261369815735742549428789138300843082086550059082835141454526618160634109969195486322015775943030060449557090064811940139431735209185996454739163555910726493597222646855506445602953689527405362207926990442391705014604777038685880527537489845359101552442292804398472642356609304810680731556542002301547846635101455995732584071355903010856718680732337369128498655255277003643669031694516851390505923416710601212618443109844041514942401969629158975457079026906304328749039997262960301209158175920051890620947063936347307238412281568760161

print(tonelli_shanks(a,p))

# 2362339307683048638327773298580489298932137505520500388338271052053734747862351779647314176817953359071871560041125289919247146074907151612762640868199621186559522068338032600991311882224016021222672243139362180461232646732465848840425458257930887856583379600967761738596782877851318489355679822813155123045705285112099448146426755110160002515592418850432103641815811071548456284263507805589445073657565381850521367969675699760755310784623577076440037747681760302434924932113640061738777601194622244192758024180853916244427254065441962557282572849162772740798989647948645207349737457445440405057156897508368531939120