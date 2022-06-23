import random


def day2():
    """ Texts regarding stake pool in Japanese & English, and general information.
    Returns:
        text(str)
    """

    text1 = """
普段はサーバ関連のインフラエンジニアとして働いています。
LinuxやチャールズさんオススメのPythonでプログラムを組んで仕事効率化の取り組みもしています。

#Cardano の構想やシステムに賛同し、ステークプールオペレータとしても貢献してきたいと思っていますのでよろしくお願いします！
"""

    text1e = """
I usually work as a server-related infrastructure engineer.
My focus is to improve work efficiency by programming in Linux and Python recommended by Charles.

I would like to support the concept and system of #Cardano and contribute to it as a stakepool operator!
"""

    text2 = """
SUGAR ステークプールは2020年8月に立ち上げた、東京とロンドン設置のプールです。
これまでに500以上のブロック生成の成功実績があります。
安定運用し、安心してご委任いただけるよう努力してまいりますので、委任のご検討、ご協力のほどよろしくお願いします。
"""

    text2e = """
SUGAR Stake Pool was launched in August 2020 and is located in Tokyo and London.
We have successfully generated over 500 blocks.
SUGAR Stake Pool will continue to strive for stable and secure operation, so please consider delegating and cooperate with us.
"""

    text3 = """
SUGAR ステークプールは「段階的な手数料」で運営しております。
ステークが10M集まるまでは0%で、委任のご協力をいただいている皆様へのメリット重視で運用いたします。

詳細についてはブログもご覧ください。
https://sugarstakepool.jp/2021/09/18/pool_fee/
"""

    text3e = """
SUGAR Stake Pool is operated on a "tiered fee" basis.
The fee will be 0% until 10M stakes are collected to focus on the benefits to those who have been cooperating in the delegation.

For more information, please also visit our blog.
https://sugarstakepool.jp/2021/09/18/pool_fee/
"""

    text4 = """
堅牢な #Cardano システムのため、分散化が重要です。
SUGAR ステークプールでは、下記の様な考えで運営しております。

- 委任者や参加者が増えてほしい
- 小さいプールが育つのを応援したい
- 複数プール運営をする前に、その他の対応での検討が大事
"""

    text4e = """
Decentralization is important for a robust #Cardano system.
SUGAR Stake Pool is operated with the following ideas.

- Welcome more delegators and participants.
- Be supportive to growth of small pools.
- Before running multiple pools, it is important to consider in other methods.
"""

    text5 = """
プールの運用実績はこちらへまとめております。
報酬のシミュレーションは参考値としてご活用ください。

#Cardano
https://sugarstakepool.jp/dashboard/
"""

    text5e = """
Pool statistics are summarized here.
Please use the reward simulation as a reference.

#Cardano
https://sugarstakepool.jp/dashboard/
"""

    text6 = """
$ADA や暗号資産の売買の際、取引所に比べ販売所はスプレッドがあるため検討が必要です。

購入と売却のできる価格差が開いていることがあり、これが実質手数料となるため、気づかないうちに多くの手数料を払っていないかご注意ください。
"""

    text7 = """
#BITPOINT は2021年に日本で初めて#Cardano $ADA の取り扱いを開始しました。
当初は販売所のみの対応でしたが、BITPOINT PROで取引所形式での売買ができます。
"""

    text8 = """
当プールの運用や実績、毎エポックのレポートなどの詳細は、ホームページでご確認いただければ幸いです。
https://sugarstakepool.jp/category/journal/
"""

    text_list = [text1, text2, text3, text4, text5, text6, text7, text8,
                 text1e, text2e, text3e, text4e, text5e]
    return random.choice(text_list)


def day3():
    """ Texts regarding staking (and Cardano) in general in Japanese.
    Returns:
        text(str)
    """

    text1 = """
#Cardano $ADA を購入した後はぜひステーキングをご検討ください！
ホールドしたままの方は、毎エポック（5日に1度）の報酬、年間数%の利益を逃しているのでもったいないです。
ステーキングによる資産を失うリスクはなく、「〜日間は取り出せない」などのロックもありません。
"""

    text2 = """
飽和したプールにご注意ください。
以前検証した時は、本来もらえていた報酬より確実に減るという結果になりました。
飽和したプールではステークが増えるほど報酬は少なくなります。
"""

    text3 = """
宣言済み誓約に達していないプールについてです。
「オペレータが宣言した出資額」に「実際の出資」が満たない場合、報酬がもらえなくなってしまいますのでご注意ください。
#PoolTool ではバツマークがついています。

https://pooltool.io/
"""

    text4 = """
プールにおける報酬分配までの流れ
1エポック目: 有効ステーク量に応じ、ブロック生成スケジュールがランダムに割り当てられる。
2エポック目: スケジュールされたブロックを生成する。
3エポック目: パフォーマンスに基づいて報酬が計算される。
4エポック目: 報酬がステークホルダーに分配される。
"""

    text5 = """
チャールズさん語録(1)
"Don’t pay attention to the noise, follow the facts."
「雑音を気にせず、事実を追いかけましょう」
"""

    text6 = """
チャールズさん語録(2)
"Don’t be evil" to "Can’t be evil"
「悪になるな」(と戒める社会)から「悪になれない」（仕組み）へ。
"""

    text7 = """
初めての委任と報酬
初めて委任された方は、ちゃんとステーキングができている状態なのか心配になるかもしれません。

仕組み上、初の委任後、初の報酬は15〜20日後になります。
以降は5日ごとに報酬を獲得していくことになりますので、少しの間お待ちいただければと思います。

#Cardano $ADA
"""

    text8 = """
もし #Cardano $ADA の委任操作が正常にできているか不安になった場合は、お気軽にお問い合わせください。
例）報酬が思った通り確認できない、いくらの報酬が入っているはずか、など
"""

    text9 = """
委任ができた後は
追加操作なしで、1エポックごとに報酬が入り続けることになります。（1エポックという #Cardano 時間があり、1エポック=5日に相当します）
得た報酬も含め委任をしている状態（複利運用）となり、1エポック毎の報酬にはばらつきが出るものの、年利数%が期待できます。
"""

    text10 = """
#Cardano ステーク・プールを探すには
#PoolTool はシンプルな表示で、プールの手数料の一覧や、その他判断に必要な情報がしっかりと載っています。
嬉しい報酬履歴一覧の機能、プールのブロック生成状況、ROS傾向などが確認できます。

https://pooltool.io/
"""

    text11 = """
#Cardano では投票することで報酬を得ることができます。
「報酬は支払い用の（受け取り）アドレスではなく、報酬アドレス（ステークキー）に送信されるため、報酬の残高が増加します。」

#ProjectCatalyst では、資金提供する開発やプロジェクトへ誰でも提案と投票ができます。
"""

    text12 = """
#ProjectCatalyst の提案と投票
報酬を除く500 ADA以上あるウォレットは投票する資格があります。
そのため、ほぼ誰でも、 #Cardano の今後に直接関われる重要な意思決定です。
"""

    text13 = """
委任とは
$ADA ホルダーが自身のADAに付随するステークをステーク・プールに預ける行為です。
これにより、サーバ運用しなくてもネットワークに参加し、委任したステーク量に応じてブロック生成に関わることができます。
* ADAを「送金」することではないため、委任によるADAの損失はありません。
"""

    text14 = """
ステーク・プールがブロック生成を担う「スロット・リーダ」に選ばれる確率は、そのプールに委任されたステークの量に比例します。
ブロック生成に成功させることでプールは報酬を受け取り、その報酬は各メンバーが委任したステークの量に応じて分配されます。
"""

    text15 = """
未発行のADAはリザーブと呼ばれ、5日ごとに一定の割合で取り出されるため市場の供給量は増えていきます。
#Cardano $ADA の最大供給量は45,000,000,000と決まっており、無尽蔵に増やされることによる値崩れの心配はありません。
"""

    text16 = """
$ADA は最初のコンピュータプログラマとされる数学者のエイダラブレスにちなんでつけられた名前です。
ウォレットでも小数点以下の細かい残高を見ることがありますが、1 Ada = 1,000,000 Lovelaceという単位でも表現されます。

#Cardano
"""

    text_list = [text1, text2, text3, text4,
                 text5, text6, text7, text8, text9, text10, text11, text12, text13, text14, text15, text16]
    return random.choice(text_list)


def day4():
    """ Texts regarding staking (and Cardano) in general in English.
    Returns:
        text(str)
    """

    text1 = """
After you buy #Cardano $ADA, please consider staking it!
If you are still holding, you are missing out on the reward of every epoch (every 5 days)!
There is no risk of losing your assets by staking, and your asset won't be locked.
"""

    text2 = """
Beware of saturated pools.
When I verified this before, I found that the rewards were definitely less than what I had originally received.
In a saturated pool, the more stakes delegated, the less reward you get.
"""

    text3 = """
This is about pools that have not reached their declared pledges.
Please note that if the Actual Pledge doesn't reach the amount of Declared Pledge by the operator, you will not receive any reward.
#PoolTool shows an X on such a pool.

https://pooltool.io/
"""

    text4 = """
Rewards delivery:

Epoch 1: Each pool is randomly assigned block generation schedules based on amount of its active stake.
Epoch 2: Scheduled blocks are minted by the pool.
Epoch 3: Reward is calculated based on performance.
epoch 4: Rewards are delivered to stake holders.
"""

    text5 = """
"Don’t pay attention to the noise, follow the facts." - Charles Hoskinson
"""

    text6 = """
"Don’t be evil" to "Can’t be evil" - Charles Hoskinson
"""

    text7 = """
For the first time of delegation, you may be worried about whether you are in a proper staking condition.

After your first delegation, your first reward will come after 15-20 days.
After that, you will earn rewards every 5 days, so please wait for a while.

#Cardano
"""

    text8 = """
If you are not sure if your #Cardano $ADA delegation operation is working properly, please feel free to contact us.
E.g., Can't see reward as expected, how much reward is expected, etc.
"""

    text9 = """
After you have delegated, you will continue to be rewarded for each epoch without any additional action.
There is a #Cardano time called 1 epoch, where 1 epoch equals 5 days.
You can earn several % of profit per year, although the reward per epoch may vary.
"""

    text10 = """
How to find a #Cardano stake pool
#PoolTool has a simple display, with a good list of pool fees and other information you need to make a decision.
It has a nice reward history list feature, the pool's block generation status, and ROS trends.

https://pooltool.io/
"""

    text11 = """
In #Cardano, you can earn rewards by voting.
"Rewards are sent to the reward address (stakekey), not the payment (receipt) address, so your reward balance will grow."

With #ProjectCatalyst, anyone can propose/vote for developments and projects to be funded.
"""

    text12 = """
Proposal and vote for #ProjectCatalyst
Wallets with 500 ADA or more, excluding rewards, are eligible to vote.
So almost anyone can be directly involved in the future of #Cardano.
"""

    text13 = """
Delegation in #Cardano is the act of ADA holders depositing stakes associated with $ADA into stake pools.
This allows to participate in maintaining network without running servers.
* There is no loss of ADA due to delegation, as it is not "transferring" actual ADA.
"""

    text14 = """
Probability of a stake pool being chosen as a "slot leader" responsible for block generation is proportional to its stake.
The pool is rewarded for successful block generation.
The reward is distributed according to the amount of stake each member has delegated.
"""

    text15 = """
Unissued ADA is called reserve, and is taken out at a fixed rate every five days, thus increasing the supply in the market.
The maximum supply of #Cardano $ADA is set at 45,000,000,000, so there is no need to worry about price collapse due to over supply.
"""

    text16 = """
$ADA is named after Ada Lovelace, a mathematician who is considered to be the first computer programmer.
You may also see fine decimal balances in wallets, which are also expressed in units of 1 Ada = 1,000,000 Lovelace.

#Cardano
"""

    text_list = [text1, text2, text3, text4,
                 text5, text6, text7, text8, text9, text10, text11, text12, text13, text14, text15, text16]
    return random.choice(text_list)


def day5():
    """ Texts for useful information for staking life
    Returns:
        text(str)
    """

    text1 = """
#Cardano ユーザ向けに、安全なウォレット管理のためのガイドラインです。
思いもよらない盗難や事故防止のためにも、お時間のある時にぜひご一読ください！
暗号資産全般はもちろん、一般的なセキュリティ対策の参考になります。

https://bit.ly/3EtNgt6
"""

    text1e = """
Guidelines for secure wallet management for #Cardano users.
To prevent unexpected theft and accidents, please take a moment to have a look!
This is a good reference for cryptographic assets in general as well as general security measures.

https://bit.ly/3BtV1x9
"""

    text2 = """
「委任をするだけでなぜ報酬を得ることができるのか？報酬はどこからくるのか？」など、
ステーキングに関して、いただいたご質問にお答えした内容の記事です。
疑問の解消に貢献できれば嬉しいです！

#Cardano
https://sugarstakepool.jp/2021/08/15/delegation-reward/
"""

    text2e = """
"Why do I get paid just for delegating?"
"Where does reward come from?"
If you have any questions about staking, I hope this blog will help.

#Cardano
https://sugarstakepool.jp/2021/08/15/delegation-reward/
"""

    text3 = """
初めてプールに委任した時、手数料、誓約金など、色々な数値があり困惑したことがあります。
委任者目線でどこをみれば良いのか、どんなプールに気を付けるといいのかを書いた記事になります。
プール選びのご参考の一つにしていただけると嬉しいです。

#Cardano
https://sugarstakepool.jp/2021/04/10/how-to-select-pool/
"""

    text3e = """
When I first staked with a pool, I wasn't familiar with various numbers of fees, pledges, etc.
This blog is about what to look for and what pools to watch out for from the perspective of a delegator, hopefully to help in finding a pool.

#Cardano
https://sugarstakepool.jp/2021/04/10/how-to-select-pool/
"""

    text4 = """
投票をすることで、今後の報酬へ影響があるかもしれません。
投票やガバナンス、ボルテールなどについて概要レベルでとまとめてみました。
投票方法や関連リンクもありますので、これを機会に参加者が増えればと願っています。

#Cardano
https://sugarstakepool.jp/2021/07/11/catalyst/
"""

    text5 = """
PoolToolのダッシュボードで #Cardano 全体、プールの一覧等をみることができます。
加えて、情報の通知をしてくれるPoolToolBotや、報酬履歴出力の機能があります。
用語の整理と、機能の使い方を記事にしました！

#Cardano
https://sugarstakepool.jp/2021/04/08/pooltool/
"""

    text5e = """
#Cardano network and pool statistics are listed on PoolTool's dashboard.
In addition, there are features such as PoolToolBot, outputting reward history, etc.
Here is a blog on terminology and how to use those features!

#Cardano
https://sugarstakepool.jp/2021/04/08/pooltool/
"""

    text6 = """
#Cardanocube は #Cardano で作られているdAppsやプロジェクトがリストされています。

カテゴリ分けされ全容がぱっと見で分かりやすいです！
各プロジェクトの概要説明もあります。

https://www.cardanocube.io/
"""

    text6e = """
#Cardanocube is a list of dApps and projects that are built on #Cardano.

It's categorized and easy to understand at a glance!
There is also an overview of all projects and dApps.

https://www.cardanocube.io/
"""

    text7 = """
ウォレットを作成した時に控えるリカバリフレーズは何よりも大事なものです。

PCやスマホが壊れても別の端末で復元することができる唯一の方法です。
これが第三者に知られることは資産を渡すこととほぼイコールになるため大切に保管します。

#Cardano
"""

    text8 = """
#ProjectCatalyst では、$ADA ホルダーが #Cardano の開発、ガバナンス、コミュニティ活動などに関わることができます。

操作手順や注意点などを記事にしております。レポートという形でご参考いただければ幸いです。

https://sugarstakepool.jp/2021/06/05/catalyst-voting/
"""

    text9 = """
2022年6月、 #CardanoFoundation は Linux Foundation の ゴールドメンバーになりました。
オープンソースを通じ、大規模なイノベーションの実現を目指します。

https://linuxfoundation.org/our-members-are-our-superpower-2/
"""

    text_list = [text1, text2, text3, text4, text5, text6, text7, text8, text9,
                 text1e, text2e, text3e, text5e, text6e]
    return random.choice(text_list)
