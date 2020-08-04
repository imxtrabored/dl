from core.advbase import *
from slot.a import *

def module():
    return Gala_Euden


class Gala_Euden(Adv):
    comment = 'c2+fs'
    conf = {}
    conf['acl'] = """
        `dragon, s=1
        `s1, fsc or s=2
        `s2, fsc
        `s3, fsc
        `s4, fsc
        `fs,seq=2 and cancel
    """
    coab = ['Dagger2','Dagger','Peony']
    share = ['Ranzal']
    conf['afflict_res.paralysis'] = 0

    def prerun(self):
        self.s2.autocharge_init(15873).on()
        if self.condition('draconic charge'):
            self.dragonform.dragon_gauge += 500
        Modifier('a3','dt','hecc',1/0.7-1).on()
        self.dragonlight_spd = Spdbuff('dragonlight',0.1,-1,wide='self')
        Event('dragon').listener(self.a3_on)
        Event('idle').listener(self.a3_off)

    def a3_on(self, e):
        if not self.dragonlight_spd.get():
            self.dragonlight_spd.on()

    def a3_off(self, e):
        if self.dragonlight_spd.get():
            self.dragonlight_spd.off()

    def s1_proc(self, e):
        if self.condition(f'{e.name} buff for 10s'):
            Teambuff(e.name,0.20,10,'att').no_bufftime().on()

    def s2_proc(self, e):
        Event('defchain')()
        self.afflics.paralysis(e.name, 120, 0.97)


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)