from showcase.cluster2_showcase import cluster2_score_length, cluster2_test, cluster2_showcase
from dbo.data_repository import DataRepository
from showcase.mobile_showcase import mobile_showcase
from showcase.crypto_showcase import crypto_showcase
from utils.utils import Mailbox


if __name__ == "__main__":
    Mailbox.debugLevel = 1

    # .meta files are shorter - exchange later for normal size archives
    data_sources = [
        {"dirname": "3dprinting", "url": "https://archive.org/download/stackexchange/3dprinting.meta.stackexchange.com.7z"},
        {"dirname": "android", "url": "https://archive.org/download/stackexchange/android.meta.stackexchange.com.7z"},
        {"dirname": "apple_cmp1", "url": "https://archive.org/download/stackexchange/apple.stackexchange.com.7z"},
        {"dirname": "android_cmp1", "url": "https://archive.org/download/stackexchange/android.stackexchange.com.7z"},
        {"dirname": "windowsphone_cmp1", "url": "https://archive.org/download/stackexchange/windowsphone.stackexchange.com.7z"},
        {"dirname": "bitcoin", "url": "https://archive.org/download/stackexchange/bitcoin.stackexchange.com.7z"},
        {"dirname": "ethereum", "url": "https://archive.org/download/stackexchange/ethereum.stackexchange.com.7z"},
    ]

    data_repository = DataRepository(_data_sources=data_sources, _data_directory="../../data", _caching=True)
    data_repository.load_data_sets()

    mobile_showcase(data_repository)
    crypto_showcase(data_repository)
    cluster2_showcase()
