"""
From: in.org.npci.upiapp.nfc.models
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class AcknowledgeValue:
    signature: str


@dataclass
class App:
    name: str


@dataclass
class AuthData:
    country: str
    currency: str
    id: str
    mcc: str
    product: str
    purseCertificate: str
    signature: str
    type: str


@dataclass
class AssertIdentity(AuthData):
    seq: str


@dataclass
class CheckTransferLimits:
    pvr: str


@dataclass
class ContextData:
    amount: str
    balance: str
    challenge: str
    country: str
    currency: str
    id: str
    isPayer: str
    mcc: str
    payeeInfo: str
    payerInfo: str
    product: str
    seq: str
    state: str
    type: str


@dataclass
class DeviceData:
    deviceTime: str
    deviceType: str
    manufacturer: str
    model: str
    osVersion: str
    platform: str


@dataclass
class DeviceDetails:
    app: App
    deviceData: DeviceData
    usecase: "Usecase"


@dataclass
class HandshakeModel:
    supportedFlags: int
    supportedProtocolVersions: list[int]


@dataclass
class LegRequest:
    vtpRequest: "VtpRequest"


@dataclass
class LegResponse:
    vtpResponse: "VtpResponse"


@dataclass
class PayeeInfo:
    deviceId: str
    mobile: str
    payeeID: str
    payeeInfo: str
    payeeVPA: str
    referenceId: str


@dataclass
class PayerInfo:
    amount: str
    country: str
    currency: str
    deviceId: str
    liteBalanceAmount: str
    maxTransferLimit: str
    mobile: str
    offlineActivated: bool
    payerID: str
    payerInfo: str
    payerVPA: str
    referenceId: str
    timeStamp: str


@dataclass
class PurseInfo:
    balance: str
    challenge: str
    country: str
    currency: str
    id: str
    mcc: str
    product: str
    seq: str
    state: str
    type: str


@dataclass
class RequestValue(AcknowledgeValue): ...


@dataclass
class StartCredit:
    signature: str
    txnId: str


@dataclass
class StartDebit:
    txnId: str


@dataclass
class StartTransferData:
    amount: str
    currency: str
    payeeVpa: str
    payee_id: str
    payee_seq: str
    payerVpa: str
    payer_id: str
    payer_seq: str
    timestamp: str


@dataclass
class TransferValue(AcknowledgeValue): ...


@dataclass
class TxnDetails:
    amount: str
    dateTime: str
    isPayerTxn: bool
    payeeQR: str
    payeeVPA: str
    payerQR: str
    payerVPA: str
    status: str
    txnId: str


@dataclass
class Usecase:
    category: str
    type: str


@dataclass
class VerifyIdentity:
    """
    it is empty in source
    """

    ...


@dataclass
class VtpRequest:
    data: dict[str, Any]
    type: str


@dataclass
class VtpResponse(VtpRequest):
    status: str
