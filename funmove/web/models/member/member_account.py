# -*- coding: utf-8 -*-
from django.db import models
from member_type import MemebrType
from uuidfield import UUIDField

# 第一版本：
# 為登入使用者，此用此Table記錄，密碼為None。
# 不處理信箱驗證
# 會員類型 應為非註冊人員

# 本網站 帳號登入
class MemberAccount(models.Model):
    # TODO : MemberAccount 由於django尚不支援 BigInt Auto_increment，所以後續要處理
    id = models.BigIntegerField(primary_key=True)
    # email登入
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=45, default=None)
    # 電話號碼
    cell_phone = models.CharField(max_length=11, null=False, blank=False)
    # 外鍵，關聯到 MemberType，可以知道屬於哪種MemberType
    # 透過related_name使得MemberType可以得知屬於此Type的MemebrAccount數量
    # 預設related_name會是類別名稱後面補上__set，因此建議有給名稱會比較好辨認
    fk_member_type = models.ForeignKey(
        'MemebrType',
        related_name='type_accounts',
        null=True,
        on_delete=models.SET_NULL)
    # 是否有驗證過手機簡訊
    phone_sms_verification = models.BooleanField(default=False)
    # UUID產生驗證Key
    activation_key = UUIDField(auto=True)
    # 新增資料時會需要設定驗證的期限
    # 如果下次登入時，會判斷期限是否超過，如果超過會告知使用者需要驗證
    # 並重新產生 activation_key 與時間
    # TODO : MemberAccount 新增資料時的產生後 7天 期限
    # TODO : MemberAccount 登入帳號 query時的驗證時間與修改 (含UUID)
    key_expired = models.DateTimeField()
    create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    # 是否被刪除的註記
    deactivated = models.BooleanField(default=False)
    # 帳號可能是使用者或是後台帳號
    # TODO : MemberAccount 需要調整此部分的 新增與修改判斷
    create_account = models.CharField(max_length=45, null=False)
    update_account = models.CharField(max_length=45, null=False)
    deactivated_account = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Memebr_Account'

    def __unicode__(self):
        pass

